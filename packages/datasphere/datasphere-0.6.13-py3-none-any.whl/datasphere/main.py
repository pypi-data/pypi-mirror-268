import argparse
import sys
import grpc
import logging
import os
import tempfile

from datasphere.auth import oauth_token_env_var_1, oauth_token_env_var_2
from datasphere.client import Client, OperationError, ProgramError
from datasphere.config import parse_config, check_limits
from datasphere.files import prepare_local_modules
from datasphere.logs import configure_logging
from datasphere.pyenv import define_py_env
from datasphere.utils import check_package_version, print_logs_files
from datasphere.version import version
from datasphere.output import output, job_spec, project_spec, Format, ExecutionData, execution_data_spec

logger = logging.getLogger('datasphere.main')
# logger for things which do not go through logging, such as traceback in stderr
logger_file = logging.getLogger('datasphere_file')


def execute(args):
    cfg = parse_config(args.config)

    py_env = None
    if cfg.env.python:
        logger.debug('defining python env ...')
        py_env = define_py_env(cfg.python_root_modules, cfg.env.python)

    async_mode = args.async_

    with tempfile.TemporaryDirectory(prefix='datasphere_') as tmpdir:
        logger.debug('using tmp dir `%s` to prepare local files', tmpdir)

        if py_env:
            local_modules = [f.get_file() for f in prepare_local_modules(py_env, tmpdir)]
            # Preserve original local modules paths (before archiving).
            sha256_to_display_path = {f.sha256: p for f, p in zip(local_modules, py_env.local_modules_paths)}
        else:
            local_modules = []
            sha256_to_display_path = {}

        check_limits(cfg, local_modules)

        job_params = cfg.get_job_params(py_env, local_modules)
        if py_env:
            logger.debug('resulting conda.yaml:\n%s', job_params.env.python_env.conda_yaml)

        client = Client(args.token)

        job_id = client.create(job_params, cfg, args.project_id, sha256_to_display_path)
        op, execute_call = client.execute(job_id, async_mode=async_mode)
        logger.debug('operation `%s` executes the job', op.id)

    if not async_mode:
        client.wait_for_completion(op, execute_call)
    elif args.output != sys.stdout:
        output([ExecutionData(job_id=job_id, operation_id=op.id)], execution_data_spec, args.output, Format.JSON)


def attach(args):
    client = Client(args.token)
    # TODO: handle case of completed job, display DS job link with results.
    op, execute_call = client.execute(args.id, std_logs_offset=-1)
    client.wait_for_completion(op, execute_call)


def ls(args):
    client = Client(args.token)
    jobs = client.list(args.project_id)
    output(jobs, job_spec, args.output, args.format)


def get(args):
    client = Client(args.token)
    job = client.get(args.id)
    output([job], job_spec, args.output, args.format)


def delete(args):
    client = Client(args.token)
    client.delete(args.id)
    logger.info('job deleted')


def cancel(args):
    client = Client(args.token)
    client.cancel(args.id)


def ls_projects(args):
    client = Client(args.token)
    projects = client.list_projects(args.community_id)
    output(projects, project_spec, args.output, args.format)


def get_project(args):
    client = Client(args.token)
    project = client.get_project(args.id)
    output([project], project_spec, args.output, args.format)


def show_version(_):
    print(version)


def build_arg_parser() -> argparse.ArgumentParser:
    parser_datasphere = argparse.ArgumentParser(prog='datasphere')
    parser_datasphere.add_argument(
        '-t', '--token', required=False,
        default=os.environ.get(oauth_token_env_var_1) or os.environ.get(oauth_token_env_var_2),
        help='YC OAuth token, see https://cloud.yandex.com/docs/iam/concepts/authorization/oauth-token'
    )
    parser_datasphere.add_argument(
        '-l', '--log-level', required=False, default=logging.INFO,
        choices=[logging.getLevelName(level) for level in (logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG)],
        help='Logging level',
    )
    parser_datasphere.add_argument(
        '--log-config', required=False, type=argparse.FileType('r'), help='Custom logging config'
    )
    parser_datasphere.add_argument('--log-dir', required=False, help='Logs directory (temporary directory by default)')
    subparsers_datasphere = parser_datasphere.add_subparsers(required=True)

    parser_version = subparsers_datasphere.add_parser('version', help='Show version')
    parser_version.set_defaults(func=show_version)

    parser_project = subparsers_datasphere.add_parser('project')
    subparsers_project = parser_project.add_subparsers(required=True)

    parser_job = subparsers_project.add_parser('job')
    subparsers_job = parser_job.add_subparsers(required=True)

    def add_project_id_argument(parser):
        parser.add_argument('-p', '--project-id', required=True, help='DataSphere project ID')

    def add_id_argument(parser, help: str = 'Job ID'):
        parser.add_argument('--id', required=True, help=help)

    def add_output_argument(parser, help: str = 'Output file (stdout by default)'):
        parser.add_argument('-o', '--output', help=help, default=sys.stdout, type=argparse.FileType('w'))

    def add_format_argument(parser):
        parser.add_argument(
            '--format', help='Output format',
            choices=[e.value for e in Format],
            default=Format.TABLE.value,
        )

    parser_execute = subparsers_job.add_parser('execute', help='Execute job')
    add_project_id_argument(parser_execute)
    parser_execute.add_argument('-c', '--config', required=True, help='Config file', type=argparse.FileType('r'))
    parser_execute.add_argument('--async', action='store_true', dest='async_', help='Async mode')
    add_output_argument(parser_execute, help='File with execution data, for async mode (none by default)')
    parser_execute.set_defaults(func=execute)

    parser_attach = subparsers_job.add_parser('attach', help='Attach to the job execution')
    add_id_argument(parser_attach)
    parser_attach.set_defaults(func=attach)

    parser_list = subparsers_job.add_parser('list', help='List jobs')
    add_project_id_argument(parser_list)
    add_output_argument(parser_list)
    add_format_argument(parser_list)
    parser_list.set_defaults(func=ls)

    parser_get = subparsers_job.add_parser('get', help='Get job')
    add_id_argument(parser_get)
    add_output_argument(parser_get)
    add_format_argument(parser_get)
    parser_get.set_defaults(func=get)

    parser_delete = subparsers_job.add_parser('delete', help='Delete job')
    add_id_argument(parser_delete)
    # parser_delete.set_defaults(func=delete)  # DATASPHERE-1339

    parser_cancel = subparsers_job.add_parser('cancel', help='Cancel job')
    add_id_argument(parser_cancel)
    parser_cancel.set_defaults(func=cancel)

    parser_project_get = subparsers_project.add_parser('get', help='Get project')
    add_id_argument(parser_project_get, help='Project ID')
    add_output_argument(parser_project_get)
    add_format_argument(parser_project_get)
    parser_project_get.set_defaults(func=get_project)

    parser_project_list = subparsers_project.add_parser('list', help='List projects')
    parser_project_list.add_argument('-c', '--community-id', required=True, help='Community ID')
    add_output_argument(parser_project_list)
    add_format_argument(parser_project_list)
    parser_project_list.set_defaults(func=ls_projects)

    return parser_datasphere


def main():
    arg_parser = build_arg_parser()

    args = arg_parser.parse_args()

    logs_file_path = configure_logging(args.log_level, args.log_config, args.log_dir)
    logger.info('logs file path: %s', logs_file_path)

    try:
        args.func(args)
    except Exception as e:
        log_exception(e, logs_file_path)
        print_logs_files(logs_file_path)
        raise
    finally:
        check_package_version()


def log_exception(e: Exception, logs_file_path: str):
    title = 'Error occurred'
    md = None
    if isinstance(e, grpc.RpcError):
        md = e.args[0].initial_metadata
        title = 'RPC error occurred'
    elif isinstance(e, OperationError):
        md = e.call_which_created_op.initial_metadata()
        title = 'Operation error occurred'
    elif isinstance(e, ProgramError):
        title = 'Program error occurred'
    md_str = '\n\theaders\n' + '\n'.join(f'\t\t{h.key}: {h.value}' for h in md) if md else ''
    logger.error('%s\n\tlogs file path: %s%s', title, logs_file_path, md_str)
    logger_file.exception(e)


if __name__ == '__main__':
    main()
