import os
from datetime import timedelta
import logging
from pathlib import Path
from threading import Thread
from time import sleep
from typing import Dict, List, Optional, Tuple, TextIO, Callable

import pytz

from google.rpc.code_pb2 import _CODE
from google.protobuf.duration_pb2 import Duration
import grpc

from datasphere.api import (
    jobs_pb2 as jobs, project_job_service_pb2 as job_service, project_job_service_pb2_grpc as job_service_grpc,
    project_service_pb2_grpc as project_service_grpc, project_service_pb2 as project_service,
    project_pb2 as project, operation_pb2 as operation, operation_service_pb2 as operation_service,
    operation_service_pb2_grpc as operation_service_grpc
)

from datasphere.api import ui_endpoint
from datasphere.auth import get_md
from datasphere.channel import get_channels
from datasphere.config import Config
from datasphere.files import download_files, upload_files
from datasphere.logs import logger_program_stdout, logger_program_stderr, logger_system_log, logger_docker_stats
from datasphere.utils import query_yes_no

logger = logging.getLogger(__name__)

operation_check_interval_seconds = 5
log_read_interval_seconds = 5

loggers_map = {
    job_service.StandardStream.OUT: logger_program_stdout,
    job_service.StandardStream.ERR: logger_program_stderr,
}

system_loggers_map = {
    ".system.log": logger_system_log,
    ".docker_stats.tsv": logger_docker_stats,
}


class Client:
    oauth_token: str

    stub: job_service_grpc.ProjectJobServiceStub
    prj_stub: project_service_grpc.ProjectServiceStub
    op_stub: operation_service_grpc.OperationServiceStub

    def __init__(self, oauth_token: Optional[str] = None):
        self.oauth_token = oauth_token
        chan, op_chan = get_channels()
        self.stub = job_service_grpc.ProjectJobServiceStub(chan)
        self.prj_stub = project_service_grpc.ProjectServiceStub(chan)
        self.op_stub = operation_service_grpc.OperationServiceStub(op_chan)

    def create(
            self,
            job_params: jobs.JobParameters,
            cfg: Config,
            project_id: str,
            sha256_to_display_path: Dict[str, str],
    ) -> str:
        logger.info('creating job ...')
        data_ttl = Duration()
        data_ttl.FromTimedelta(timedelta(days=14))
        op, create_call = self.stub.Create.with_call(
            job_service.CreateProjectJobRequest(
                project_id=project_id,
                job_parameters=job_params,
                config=cfg.content,
                name=cfg.name,
                desc=cfg.desc,
                data_ttl=data_ttl,
            ),
            metadata=self.md,
        )
        op = self._poll_operation(op, create_call)
        resp = job_service.CreateProjectJobResponse()
        op.response.Unpack(resp)
        upload_files(list(resp.upload_files), sha256_to_display_path)
        logger.info('created job `%s`', resp.job_id)
        return resp.job_id

    def execute(
            self,
            job_id: str,
            std_logs_offset: int = 0,
            async_mode: bool = False,
    ) -> Tuple[operation.Operation, grpc.Call]:
        if not async_mode:
            self.read_logs(job_id, std_logs_offset)
        logger.debug('executing job ...')
        return self.stub.Execute.with_call(job_service.ExecuteProjectJobRequest(job_id=job_id), metadata=self.md)

    def list(self, project_id: str) -> List[jobs.Job]:
        return _list_entities(
            request_func=lambda page_token: self.stub.List(
                job_service.ListProjectJobRequest(project_id=project_id, page_size=50, page_token=page_token),
                metadata=self.md,
            ),
            response_field_name='jobs',
        )

    def get(self, job_id: str) -> jobs.Job:
        return self.stub.Get(job_service.GetProjectJobRequest(job_id=job_id), metadata=self.md)

    def delete(self, job_id: str):
        self.stub.Delete(job_service.DeleteProjectJobRequest(job_id=job_id), metadata=self.md)

    def cancel(self, job_id: str):
        self.stub.Cancel(job_service.CancelProjectJobRequest(job_id=job_id), metadata=self.md)
        logger.info('job is canceled')

    def get_project(self, project_id: str) -> project.Project:
        return self.prj_stub.Get(project_service.GetProjectRequest(project_id=project_id), metadata=self.md)

    def list_projects(self, community_id: str) -> List[project.Project]:
        return _list_entities(
            request_func=lambda page_token: self.prj_stub.List(
                project_service.ListProjectsRequest(community_id=community_id, page_size=50, page_token=page_token),
                metadata=self.md
            ),
            response_field_name='projects',
            page_token_field_name='next_page_token',
        )

    def wait_for_completion(self, op: operation.Operation, call_which_created_op: grpc.Call):
        logger.info('executing job ...')
        try:
            op = self._poll_operation(op, call_which_created_op)
        finally:
            op_meta = job_service.ExecuteProjectJobMetadata()
            op.metadata.Unpack(op_meta)
            self._display_job_link(op_meta.job)
        resp = job_service.ExecuteProjectJobResponse()
        op.response.Unpack(resp)
        download_files(list(resp.output_files))
        if resp.result.return_code != 0:
            raise ProgramError(resp.result.return_code)
        logger.info('job completed successfully')

    # Wait until operation is done, if it's error in operation, raise it as in case of usual gRPC call.
    def _poll_operation(self, op: operation.Operation, call_which_created_op: grpc.Call) -> operation.Operation:
        while True:
            try:
                if not op.done:
                    logger.debug('waiting for operation ...')
                    sleep(operation_check_interval_seconds)
                else:
                    if op.HasField('error'):
                        raise OperationError(op, call_which_created_op)
                    else:
                        # We are ready to unpack response.
                        return op
                op = self.op_stub.Get(operation_service.GetOperationRequest(operation_id=op.id), metadata=self.md)
            except grpc.RpcError as e:
                logger.warning('get operation %s request failed with rpc error: [%s] %s',
                               op.id, e.code(), e.details())
            except KeyboardInterrupt:
                if query_yes_no('cancel job?', default=False):
                    logger.info('cancelling job ...')
                    op_meta = job_service.ExecuteProjectJobMetadata()
                    op.metadata.Unpack(op_meta)
                    self.cancel(op_meta.job.id)
                    raise
                else:
                    logger.info('resuming job')

    def read_logs(self, job_id: str, offset: int):
        Thread(target=self._print_logs, args=[job_id, offset], daemon=True).start()

    def _print_logs(self, job_id: str, offset: int):
        """
        Server has two possible ways to return streaming response with logs:
        1) Stream will end only after job finish.
        2) Stream can end at any moment, and we have to make several requests remembering last offset.

        We don't know which way server will use, so we support both ways. Because of 1), we can read logs only
        in separate thread. Because of 2), we remember offset and make requests in infinite loop, which will
        terminate with daemon thread termination.

        In case of attach to executing job, we send offset = -1 to indicate that we want to get logs from current
        moment at time.

        Opened questions:
        - Logs read will end after downloading results (CLI process finish), some final logs may be lost.
        """

        opened_files: Dict[Path, TextIO] = {}

        try:
            while True:
                try:
                    for resp in self.stub.ReadLogs(job_service.ReadProjectJobLogsRequest(
                            job_id=job_id, offset=offset), metadata=self.md):
                        for log in resp.logs:
                            self._write_log(log, opened_files)

                        offset = resp.offset
                except grpc.RpcError as e:
                    # Sometimes stream interrupts, it's ok, and we create new one from current offset.
                    logger.debug('read logs stream interrupted ([%s] %s), creating new one from offset %d',
                                 e.code(), e.details(), offset)
                sleep(log_read_interval_seconds)
        finally:
            for f in opened_files.values():
                try:
                    f.close()
                except Exception as e:
                    logger.warning("Cannot close file", exc_info=e)

    @staticmethod
    def _write_log(log: job_service.LogMessage, opened_files: Dict[Path, TextIO]):
        try:
            lines = log.content.decode('utf8').strip().split('\n')
        except UnicodeError:
            lines = [f'[non-utf8 sequence] {log.content}']

        # program stdout/stderr
        if log.HasField("standard_stream"):
            # setting default logger for strange messages
            current_logger = loggers_map.get(log.standard_stream, logger)
            for line in lines:
                current_logger.info(line)
            return

        # custom files
        if not log.HasField("file_path"):
            for line in lines:
                logger.info(line)
            return

        # wellknown system files
        if log.file_path in system_loggers_map:
            syslog = system_loggers_map.get(log.file_path)
            for line in lines:
                syslog.handle(logging.makeLogRecord(
                    dict(
                        levelno=logging.INFO,
                        created=log.created_at.ToDatetime(tzinfo=pytz.UTC).timestamp(),
                        msg=line,
                    )))
            return

        # user files
        file_path = log.file_path
        real_path = Path(os.getcwd(), file_path).absolute()

        if real_path not in opened_files:
            try:
                real_path.parent.mkdir(exist_ok=True, parents=True)
                f = open(real_path, "w")
            except Exception as e:
                logger.warning(f"Cannot create log file {real_path}:", e)
                for line in lines:
                    logger.info(line)
                return
        else:
            f = opened_files[real_path]

        for line in lines:
            f.write(line)
            f.write("\n")
            f.flush()
        opened_files[real_path] = f

    def _display_job_link(self, job: jobs.Job):
        project_id = job.project_id
        try:
            community_id = self.get_project(project_id).community_id
        except grpc.RpcError as e:
            # Job link is nice to have, but if we couldn't get community info,
            # lets just log the error and do not crush the process.
            logger.warning('Failed to get community ID by project ID for job link generation')
            logger.exception(e)
            return
        link = f'https://{ui_endpoint}/communities/{community_id}/projects/{project_id}/job/{job.id}'
        logger.info('job link: %s', link)

    @property
    def md(self):
        return get_md(self.oauth_token)


def _list_entities(request_func: Callable, response_field_name: str, page_token_field_name: str = 'page_token') -> list:
    page_token = None
    entities = []
    while True:
        resp = request_func(page_token)
        entities += getattr(resp, response_field_name)
        page_token = getattr(resp, page_token_field_name)
        if not page_token or len(entities) == 0:
            break
    return entities


# Exception to display traceback about operation errors in similar way as usual RPC error (grpc.RpcError).
class OperationError(Exception):
    def __init__(self, op: operation.Operation, call_which_created_op: grpc.Call):
        self.op = op
        self.call_which_created_op = call_which_created_op

    def __str__(self):
        status = self.op.error
        code = _CODE.values_by_number[status.code].name
        return f'Operation returned error:\n\tstatus={code}\n\tdetails={status.message}'

    def __repr__(self):
        return str(type(self))


class ProgramError(Exception):
    def __init__(self, return_code: int):
        self.return_code = return_code

    def __str__(self):
        return f'Program returned code {self.return_code}'

    def __repr__(self):
        return str(type(self))
