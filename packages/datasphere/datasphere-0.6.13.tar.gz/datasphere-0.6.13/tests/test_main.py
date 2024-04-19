from dataclasses import dataclass
from enum import Enum
import hashlib
import logging
from unittest.mock import Mock, call
from typing import List
from pathlib import Path
from pytest import fixture, raises

import grpc

from google.protobuf.duration_pb2 import Duration

from datasphere.client import ProgramError, OperationError
from datasphere.config import VariablePath, PythonEnv as PythonEnvConfig
from datasphere.main import execute, ls
from datasphere.pyenv import PythonEnv
from datasphere.utils import PythonModule
from datasphere.api import (
    jobs_pb2 as jobs, project_job_service_pb2 as job_service, project_pb2 as project,
    project_service_pb2 as project_service, operation_pb2 as operation, operation_service_pb2 as operation_service,
)


@fixture
def main_script_content() -> bytes:
    return b'print("hello, world!")'


@fixture
def main_script_path(main_script_content) -> str:
    path = Path('main.py')
    path.write_bytes(main_script_content)
    yield str(path)
    path.unlink()


@fixture
def utils_module_content() -> bytes:
    return b'import os'


@fixture
def utils_module_path(utils_module_content) -> str:
    path = Path('utils.py')
    path.write_bytes(utils_module_content)
    yield str(path)
    path.unlink()


@fixture
def local_modules(utils_module_path) -> List[str]:
    return [utils_module_path]


@fixture
def expected_local_modules_paths(py_env) -> List[VariablePath]:
    return [VariablePath(path=p) for p in py_env.local_modules_paths]


@fixture
def expected_local_modules_files(expected_local_modules_paths):
    return [p.get_file() for p in expected_local_modules_paths]


@fixture
def py_env(local_modules) -> PythonEnv:
    return PythonEnv(
        version='',
        local_modules_paths=local_modules,
        requirements=[],
    )


@dataclass
class CodeData:
    main_script_content: bytes
    main_script_path: str
    utils_module_content: bytes
    utils_module_path: str
    local_modules: List[str]
    expected_local_modules_paths: List[VariablePath]
    expected_local_modules_files: List[jobs.File]
    py_env: PythonEnv


@fixture
def code_data(
        main_script_content,
        main_script_path,
        utils_module_content,
        utils_module_path,
        local_modules,
        expected_local_modules_paths,
        expected_local_modules_files,
        py_env,
) -> CodeData:
    return CodeData(
        main_script_content,
        main_script_path,
        utils_module_content,
        utils_module_path,
        local_modules,
        expected_local_modules_paths,
        expected_local_modules_files,
        py_env,
    )


@fixture
def input_file_content() -> bytes:
    return b'7'


@fixture
def input_file_path(tmp_path, input_file_content) -> str:
    path = tmp_path / '1.txt'
    path.write_bytes(input_file_content)
    return str(path)


@fixture
def input_file_var() -> str:
    return 'INPUT_1'


@fixture
def expected_input_files(input_file_path, input_file_var, main_script_path) -> List[jobs.File]:
    return [p.get_file() for p in (
        VariablePath(path=input_file_path, var=input_file_var),
        VariablePath(path=main_script_path),
    )]


@fixture
def output_file_path(tmp_path) -> str:
    path = tmp_path / 'result.txt'
    return str(path)


@fixture
def output_file_var() -> str:
    return 'OUTPUT_1'


@fixture
def expected_output_files(output_file_path, output_file_var) -> List[jobs.FileDesc]:
    return [p.file_desc for p in [VariablePath(path=output_file_path, var=output_file_var)]]


@fixture
def s3_mount_id() -> str:
    return 'bt10gr4c1b081bidoses'


@fixture
def dataset_id() -> str:
    return 'bt12tlsc3nkt2opg2h61'


@fixture
def dataset_var() -> str:
    return 'CIFAR'


@fixture
def expected_job_params(
        expected_input_files,
        expected_output_files,
        main_script_path,
        utils_module_path,
        utils_module_content,
        s3_mount_id,
        dataset_id,
) -> jobs.JobParameters:
    return jobs.JobParameters(
        input_files=expected_input_files,
        output_files=expected_output_files,
        s3_mount_ids=[s3_mount_id],
        dataset_ids=[dataset_id],
        cmd=f"""
python {main_script_path} 
  --features ${{{s3_mount_id}}}/features.tsv 
  --validate ${{{dataset_id}}}/val.json
  --epochs 5
""".strip(),
        env=jobs.Environment(
            python_env=jobs.PythonEnv(
                conda_yaml='name: default\ndependencies:\n- python==\n- pip\n',
                local_modules=[
                    jobs.File(
                        desc=jobs.FileDesc(path=utils_module_path),
                        sha256=get_expected_sha256(utils_module_content),
                        size_bytes=9,
                    ),
                ],
            ),
        ),
        attach_project_disk=True,
        cloud_instance_type=jobs.CloudInstanceType(name='g2.8'),
    )


@fixture
def expected_upload_files(expected_job_params) -> List[jobs.StorageFile]:
    return [
        jobs.StorageFile(file=f, url=f'https://storage.net/{f.desc.path or f.desc.var}')
        for f in list(expected_job_params.input_files) + list(expected_job_params.env.python_env.local_modules)
    ]


@fixture
def expected_download_files(expected_output_files) -> List[jobs.StorageFile]:
    return [
        jobs.StorageFile(file=jobs.File(desc=file_desc, sha256=''), url=f'https://storage.net/result_{i}')
        for i, file_desc in enumerate(expected_output_files)
    ]


@dataclass
class FilesData:
    input_file_content: bytes
    input_file_path: str
    input_file_var: str
    expected_input_files: List[jobs.File]
    expected_upload_files: List[jobs.StorageFile]
    output_file_path: str
    output_file_var: str
    expected_output_files: List[jobs.FileDesc]
    expected_download_files: List[jobs.StorageFile]


@fixture
def files_data(
        input_file_content,
        input_file_path,
        input_file_var,
        expected_input_files,
        expected_upload_files,
        output_file_path,
        output_file_var,
        expected_output_files,
        expected_download_files,
) -> FilesData:
    return FilesData(
        input_file_content,
        input_file_path,
        input_file_var,
        expected_input_files,
        expected_upload_files,
        output_file_path,
        output_file_var,
        expected_output_files,
        expected_download_files,
    )


@fixture
def community_id() -> str:
    return 'community-id'


@fixture
def project_id() -> str:
    return 'bt1u35hmfo8ok6ub1ni6'


@fixture
def cfg(
        tmp_path,
        main_script_path,
        input_file_path,
        input_file_var,
        output_file_path,
        output_file_var,
        s3_mount_id,
        dataset_id,
        dataset_var,
) -> Path:
    cfg = tmp_path / 'config.yaml'
    cfg.write_text(f"""
name: my-script
desc: Learning model using PyTorch
cmd: >  # YAML multiline string
  python {main_script_path} 
    --features ${{{s3_mount_id}}}/features.tsv 
    --validate ${{{dataset_var}}}/val.json
    --epochs 5
env:
  python: auto
inputs:
  - {input_file_path}: {input_file_var}
outputs:
  - {output_file_path}: {output_file_var}
s3-mounts:
  - {s3_mount_id}
datasets:
  - {dataset_id}:
      var: {dataset_var}
flags:
  - attach-project-disk
cloud-instance-type: g2.8
        """)
    return cfg


@fixture
def oauth_token() -> str:
    return 'AQAD...'


@fixture
def expected_metadata(oauth_token) -> list:
    return [('Authorization', f'iam-token-for {oauth_token}')]


@fixture
def create_op_id() -> str:
    return 'create-op-id'


@fixture
def expected_create_request(
        project_id,
        expected_job_params,
        cfg,
) -> job_service.CreateProjectJobRequest:
    data_ttl = Duration()
    data_ttl.FromSeconds(14 * 24 * 60 * 60)  # 14 days default TTL
    return job_service.CreateProjectJobRequest(
        project_id=project_id,
        job_parameters=expected_job_params,
        config=cfg.read_text(),
        name='my-script',
        desc='Learning model using PyTorch',
        data_ttl=data_ttl,
    )


@fixture
def job_id() -> str:
    return 'job-id'


@fixture
def expected_execute_request(job_id) -> job_service.ExecuteProjectJobRequest:
    return job_service.ExecuteProjectJobRequest(job_id=job_id)


@fixture
def execute_op_id() -> str:
    return 'exec-op-id'


@fixture
def expected_get_operation_request(execute_op_id) -> operation_service.GetOperationRequest:
    return operation_service.GetOperationRequest(operation_id=execute_op_id)


@fixture
def expected_cancel_request(job_id) -> job_service.CancelProjectJobRequest:
    return job_service.CancelProjectJobRequest(job_id=job_id)


@fixture
def expected_get_project_request(project_id) -> project_service.GetProjectRequest:
    return project_service.GetProjectRequest(project_id=project_id)


@dataclass
class RequestsData:
    expected_create_request: job_service.CreateProjectJobRequest
    create_op_id: str
    job_id: str
    expected_execute_request: job_service.ExecuteProjectJobRequest
    execute_op_id: str
    expected_get_operation_request: operation_service.GetOperationRequest
    expected_cancel_request: job_service.CancelProjectJobRequest
    community_id: str
    expected_get_project_request: project_service.GetProjectRequest
    oauth_token: str
    expected_metadata: list


@fixture
def requests_data(
        expected_create_request,
        create_op_id,
        job_id,
        expected_execute_request,
        execute_op_id,
        expected_get_operation_request,
        expected_cancel_request,
        community_id,
        expected_get_project_request,
        oauth_token,
        expected_metadata,
) -> RequestsData:
    return RequestsData(
        expected_create_request,
        create_op_id,
        job_id,
        expected_execute_request,
        execute_op_id,
        expected_get_operation_request,
        expected_cancel_request,
        community_id,
        expected_get_project_request,
        oauth_token,
        expected_metadata,
    )


class OperationStatus(Enum):
    RUNNING = 'r'
    SUCCESS = 's'
    FAILURE = 'f'


def get_op(
        op_id: str,
        job_id: str,
        project_id: str,
        expected_download_files: List[jobs.StorageFile],
        status: OperationStatus,
        program_error: bool = False,
) -> operation.Operation:
    op = operation.Operation()
    op.id = op_id
    if status == OperationStatus.FAILURE:
        op.done = True
        op.error.code = grpc.StatusCode.INTERNAL.value[0]
        op.error.message = 'Unexpected error'
    elif status == OperationStatus.SUCCESS:
        op.done = True
        op.response.Pack(job_service.ExecuteProjectJobResponse(
            output_files=expected_download_files,
            result=jobs.JobResult(return_code=1 if program_error else 0),
        ))
    op.metadata.Pack(job_service.ExecuteProjectJobMetadata(job=jobs.Job(id=job_id, project_id=project_id)))
    return op


@fixture
def running_op(execute_op_id, job_id, project_id, expected_download_files) -> operation.Operation:
    return get_op(execute_op_id, job_id, project_id, expected_download_files, OperationStatus.RUNNING)


@fixture
def successful_op(execute_op_id, job_id, project_id, expected_download_files) -> operation.Operation:
    return get_op(execute_op_id, job_id, project_id, expected_download_files, OperationStatus.SUCCESS)


@fixture
def program_error_op(execute_op_id, job_id, project_id, expected_download_files) -> operation.Operation:
    return get_op(execute_op_id, job_id, project_id, expected_download_files, OperationStatus.SUCCESS,
                  program_error=True)


@fixture
def system_error_op(execute_op_id, job_id, project_id, expected_download_files) -> operation.Operation:
    return get_op(execute_op_id, job_id, project_id, expected_download_files, OperationStatus.FAILURE)


@fixture
def output_file(tmp_path):
    return tmp_path / 'output'


@fixture
def args(cfg, project_id, oauth_token, output_file):
    f = open(output_file, 'w')
    yield Mock(config=cfg.absolute(), project_id=project_id, token=oauth_token, async_=False, format='table', output=f)
    f.close()


@fixture
def common_logs(execute_op_id) -> List[tuple]:
    return [
        ('datasphere.utils', 10, '`python` is detected as Python interpreter path by common name'),
        ('datasphere.config', 10, '`main.py` is detected as Python main module'),
        ('datasphere.main', 10, 'defining python env ...'),
        ('datasphere.main', 10, 'using tmp dir `/tmp/for/run` to prepare local files'),
        ('datasphere.main', 10, 'resulting conda.yaml:\nname: default\ndependencies:\n- python==\n- pip\n'),
        ('datasphere.client', 20, 'creating job ...'),
        ('datasphere.client', 20, 'created job `job-id`'),
        ('datasphere.client', 10, 'executing job ...'),
        ('datasphere.main', 10, 'operation `exec-op-id` executes the job'),
        ('datasphere.client', 20, 'executing job ...'),
        ('datasphere.client', 10, 'waiting for operation ...'),
    ]


@fixture
def common_logs_tail() -> List[tuple]:
    return [
        ('datasphere.client',
         20,
         'job link: '
         'https://datasphere.yandex.ru/communities/community-id/projects/bt1u35hmfo8ok6ub1ni6/job/job-id'),
    ]


def get_expected_sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def mock_metadata(mocker):
    mocker.patch('datasphere.client.get_md', lambda token: [('Authorization', f'iam-token-for {token}')])


def mock_channel(mocker):
    mocker.patch('datasphere.client.get_channels', lambda: (None, None))


def get_stub(mocker):
    return mocker.patch('yandex.cloud.datasphere.v2.jobs.project_job_service_pb2_grpc.ProjectJobServiceStub')()


def get_op_stub(mocker):
    return mocker.patch('yandex.cloud.operation.operation_service_pb2_grpc.OperationServiceStub')()


def get_prj_stub(mocker):
    return mocker.patch('yandex.cloud.datasphere.v2.project_service_pb2_grpc.ProjectServiceStub')()


def get_execute_mocks(mocker, code_data, files_data, requests_data, execute_op, get_op_side_effects: list):
    define_py_env = mocker.patch('datasphere.main.define_py_env')
    define_py_env.return_value = code_data.py_env

    run_tmp_dir = Path('/tmp/for/run')
    mocker.patch('tempfile.TemporaryDirectory', lambda *args, **kwargs: run_tmp_dir)

    prepare_local_modules = mocker.patch('datasphere.main.prepare_local_modules')
    prepare_local_modules.return_value = code_data.expected_local_modules_paths

    upload_files = mocker.patch('datasphere.client.upload_files')
    download_files = mocker.patch('datasphere.client.download_files')

    mock_metadata(mocker)
    mock_channel(mocker)

    stub = get_stub(mocker)

    create_op = operation.Operation(id=requests_data.create_op_id, done=True)
    create_op.response.Pack(job_service.CreateProjectJobResponse(
        job_id=requests_data.job_id,
        upload_files=files_data.expected_upload_files,
    ))

    rpc_call_mock = ...

    stub.Create.with_call.return_value = create_op, rpc_call_mock

    stub.Execute.with_call.return_value = execute_op, rpc_call_mock

    op_stub = get_op_stub(mocker)
    op_stub.Get.side_effect = get_op_side_effects

    mocker.patch('datasphere.client.operation_check_interval_seconds', return_value=0)
    mocker.patch('datasphere.client.log_read_interval_seconds', return_value=0)

    prj_stub = get_prj_stub(mocker)
    prj_stub.Get.return_value = project.Project(community_id=requests_data.community_id)

    return define_py_env, prepare_local_modules, run_tmp_dir, stub, upload_files, op_stub, download_files, prj_stub


class ExecutionStatus(Enum):
    SUCCESS = 's'
    SYSTEM_ERROR = 'se'
    PROGRAM_ERROR = 'pe'
    CANCEL = 'c'


def assert_common_mocks_calls(
        define_py_env,
        prepare_local_modules,
        run_tmp_dir,
        stub,
        upload_files,
        op_stub,
        download_files,
        prj_stub,
        code_data,
        files_data,
        requests_data,
        get_op_side_effects: list,
        execution_status: ExecutionStatus,
):
    define_py_env.assert_called_once_with([PythonModule(path=code_data.main_script_path)], PythonEnvConfig())

    prepare_local_modules.assert_called_once_with(code_data.py_env, run_tmp_dir)

    stub.Create.with_call.assert_called_once_with(
        requests_data.expected_create_request, metadata=requests_data.expected_metadata
    )

    upload_files.assert_called_once_with(
        files_data.expected_upload_files,
        {'de2abade832c8e350a1bdc98cfcdb1e202ac4749c5fc51a4a970d41736b6df5c': 'utils.py'},
    )

    stub.Execute.with_call.assert_called_once_with(
        requests_data.expected_execute_request, metadata=requests_data.expected_metadata
    )

    op_stub.Get.assert_has_calls(
        [
            call(requests_data.expected_get_operation_request, metadata=requests_data.expected_metadata)
        ] * len(get_op_side_effects)
    )

    prj_stub.Get.assert_called_once_with(
        requests_data.expected_get_project_request, metadata=requests_data.expected_metadata
    )

    if execution_status == ExecutionStatus.CANCEL:
        stub.Cancel.assert_called_once_with(requests_data.expected_cancel_request,
                                            metadata=requests_data.expected_metadata)
        download_files.assert_not_called()
    elif execution_status == ExecutionStatus.SYSTEM_ERROR:
        download_files.assert_not_called()
    else:
        download_files.assert_called_with(files_data.expected_download_files)


def test_successful_run(
        mocker, caplog,
        code_data, files_data, requests_data,
        running_op, successful_op,
        cfg, args, common_logs, common_logs_tail,
):
    get_op_side_effects = [running_op, successful_op]  # wait 1 time then get result

    mocks = get_execute_mocks(mocker, code_data, files_data, requests_data, running_op, get_op_side_effects)

    caplog.set_level(logging.DEBUG)

    execute(args)

    assert_common_mocks_calls(
        *(mocks + (code_data, files_data, requests_data, get_op_side_effects)),
        execution_status=ExecutionStatus.SUCCESS,
    )

    assert caplog.record_tuples == common_logs + [
        ('datasphere.client', 10, 'waiting for operation ...'),
    ] + common_logs_tail + [
        ('datasphere.client', 20, 'job completed successfully'),
    ]


def test_program_failed_run(
        mocker, caplog,
        code_data, files_data, requests_data,
        running_op, program_error_op,
        cfg, args, common_logs, common_logs_tail,
):
    get_op_side_effects = [program_error_op]

    mocks = get_execute_mocks(mocker, code_data, files_data, requests_data, running_op, get_op_side_effects)

    caplog.set_level(logging.DEBUG)

    with raises(ProgramError, match='Program returned code 1'):
        execute(args)

    assert_common_mocks_calls(
        *(mocks + (code_data, files_data, requests_data, get_op_side_effects)),
        execution_status=ExecutionStatus.PROGRAM_ERROR,
    )

    assert caplog.record_tuples == common_logs + common_logs_tail


def test_system_failed_run(
        mocker, caplog,
        code_data, files_data, requests_data,
        running_op, system_error_op,
        cfg, args, common_logs, common_logs_tail,
):
    get_op_side_effects = [system_error_op]

    mocks = get_execute_mocks(mocker, code_data, files_data, requests_data, running_op, get_op_side_effects)

    caplog.set_level(logging.DEBUG)

    with raises(OperationError, match='Operation returned error:\n\tstatus=INTERNAL\n\tdetails=Unexpected error'):
        execute(args)

    assert_common_mocks_calls(
        *(mocks + (code_data, files_data, requests_data, get_op_side_effects)),
        execution_status=ExecutionStatus.SYSTEM_ERROR,
    )

    assert caplog.record_tuples == common_logs + common_logs_tail


def test_canceled_run(
        mocker, caplog,
        code_data, files_data, requests_data,
        running_op,
        cfg, args, common_logs, common_logs_tail
):
    get_op_side_effects = [KeyboardInterrupt]

    mocks = get_execute_mocks(mocker, code_data, files_data, requests_data, running_op, get_op_side_effects)

    mocker.patch('datasphere.utils.input', lambda _: 'Y')  # cancel approved

    caplog.set_level(logging.DEBUG)

    try:
        execute(args)
    except KeyboardInterrupt:
        pass

    assert_common_mocks_calls(
        *(mocks + (code_data, files_data, requests_data, get_op_side_effects)),
        execution_status=ExecutionStatus.CANCEL,
    )

    assert caplog.record_tuples == common_logs + [
        ('datasphere.client', 20, 'cancelling job ...'),
        ('datasphere.client', 20, 'job is canceled'),
    ] + common_logs_tail


def test_list(mocker, requests_data, project_id, args, output_file):
    mock_metadata(mocker)
    mock_channel(mocker)
    stub = get_stub(mocker)
    _ = get_op_stub(mocker)
    _ = get_prj_stub(mocker)

    def list_responses(request: job_service.ListProjectJobRequest, metadata):
        return {  # client page token to response
            '': job_service.ListProjectJobResponse(jobs=[jobs.Job(id='1'), jobs.Job(id='2')], page_token='abc'),
            'abc': job_service.ListProjectJobResponse(jobs=[jobs.Job(id='3'), jobs.Job(id='4')], page_token='xyz'),
            'xyz': job_service.ListProjectJobResponse(jobs=[jobs.Job(id='5')]),
        }[request.page_token]

    # We use function instead of list of responses because otherwise responses will not have real type,
    # but mock type instead, which will cause error in protobuf type check.
    stub.List.side_effect = list_responses

    ls(args)

    stub.List.assert_has_calls([
        call(
            job_service.ListProjectJobRequest(project_id=project_id, page_size=50),
            metadata=requests_data.expected_metadata
        ),
        call(
            job_service.ListProjectJobRequest(project_id=project_id, page_size=50, page_token='abc'),
            metadata=requests_data.expected_metadata,
        ),
        call(
            job_service.ListProjectJobRequest(project_id=project_id, page_size=50, page_token='xyz'),
            metadata=requests_data.expected_metadata,
        ),
    ])

    args.output.flush()
    assert output_file.read_text() == """
  ID  Name    Description    Created at    Finished at    Status                  Created by
----  ------  -------------  ------------  -------------  ----------------------  ------------
   1                                                      JOB_STATUS_UNSPECIFIED
   2                                                      JOB_STATUS_UNSPECIFIED
   3                                                      JOB_STATUS_UNSPECIFIED
   4                                                      JOB_STATUS_UNSPECIFIED
   5                                                      JOB_STATUS_UNSPECIFIED
"""[1:]
