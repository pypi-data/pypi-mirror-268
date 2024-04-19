import enum
import os
from dataclasses import dataclass, field
from functools import partial
from io import StringIO
import logging
from pathlib import Path
from re import compile
from typing import Any, BinaryIO, TextIO, Callable, Dict, List, Optional, Union
import yaml

from envzy import ModulePathsList

from datasphere.api import jobs_pb2 as jobs
from datasphere.utils import (
    get_sha256_and_size, humanize_bytes_size, parse_human_size, parse_python_main_module, PythonModule,
)

logger = logging.getLogger(__name__)


@dataclass
class VariablePath:
    path: str
    var: Optional[str] = None

    _file: jobs.File = field(init=False, default=None)

    @property
    def file_desc(self) -> jobs.FileDesc:
        return jobs.FileDesc(path=self.path, var=self.var)

    def get_file(self, f: Optional[BinaryIO] = None) -> jobs.File:
        # TODO: one can call get_file() then get_file(f) on single file; fix semantics
        if self._file:
            return self._file

        if f:
            self._file = self._read_file(f)
        else:
            with open(self.path, 'rb') as f:
                self._file = self._read_file(f)
        return self._file

    def _read_file(self, f: BinaryIO) -> jobs.File:
        sha256, size = get_sha256_and_size(f)
        return jobs.File(desc=self.file_desc, sha256=sha256, size_bytes=size)


@dataclass
class Password:
    text: str
    is_secret: bool


@dataclass
class DockerImage:
    url: str
    username: Optional[str]
    password: Optional[Password]

    @property
    def proto(self) -> jobs.DockerImageSpec:
        spec = jobs.DockerImageSpec()
        spec.image_url = self.url
        username = self.username
        if username is not None:
            spec.username = username
        password = self.password
        if password is not None:
            if password.is_secret:
                spec.password_ds_secret_name = password.text
            else:
                spec.password_plain_text = password.text
        return spec


@dataclass
class PythonEnv:
    @dataclass
    class PipOptions:
        extra_index_urls: List[str] = field(default_factory=list)
        trusted_hosts: List[str] = field(default_factory=list)
        no_deps: bool = False

    # Python interpreter version
    version: Optional[str] = None

    # Requirements file (PyPI packages)
    requirements: Optional[Path] = None

    # List of Python root modules, or entry points. In most cases root module is single and declared with
    # `python <root_module_path> ...` or `python -m <root_module_name> ...`.
    #
    # But sometimes, other root modules can be specified in program arguments or hardcoded, i.e. for ML libraries common
    # scenario is `python -m <lib_module> <user_script_path>` – library code in main module and user declaration in
    # separate file. Or, for instance, main script can launch other root scripts in subprocesses.
    #
    # Main module is defined automatically using heuristics and additional root modules, if present, are merged with it.
    #
    # For us, it is important to know root modules not only to pass them to server but also to derive full namespace
    # for envzy explorer. Resulting namespace will be merged from all root module namespaces.
    #
    # Mutually exclusive with `local_modules_paths`.
    root_modules_paths: Optional[ModulePathsList] = None

    # Full list of user Python scripts (a.k.a. 'local project', 'local code').
    # Mutually exclusive with `root_modules_paths`.
    local_modules_paths: Optional[ModulePathsList] = None

    # Options for pip, will be applied on server during environment setup
    pip_options: Optional[PipOptions] = None

    @property
    def is_fully_manual(self) -> bool:
        return all(x is not None for x in (self.version, self.requirements, self.local_modules_paths))


@dataclass
class Environment:
    vars: Optional[Dict[str, str]]
    docker_image: Optional[Union[str, DockerImage]]  # Image resource ID or image URL
    python: Optional[PythonEnv]


@dataclass
class Config:
    cmd: str
    inputs: List[VariablePath]
    outputs: List[VariablePath]
    s3_mounts: List[VariablePath]
    datasets: List[VariablePath]
    env: Environment
    cloud_instance_type: str
    attach_project_disk: bool
    content: str
    name: Optional[str] = None
    desc: Optional[str] = None
    working_storage: Optional[jobs.ExtendedWorkingStorage] = None

    python_root_modules: List[PythonModule] = field(init=False, default_factory=list)

    def __post_init__(self):
        def get_vars(paths: List[VariablePath], with_non_vars: bool = False) -> List[str]:
            result = [v.var for v in paths if v.var is not None]
            if with_non_vars:
                result += [v.path for v in paths]
            return result

        self.__vars = \
            get_vars(self.inputs) + get_vars(self.outputs) + \
            get_vars(self.s3_mounts, with_non_vars=True) + get_vars(self.datasets, with_non_vars=True)

        if len(self.__vars) != len(set(self.__vars)):
            raise ValueError('variables in config should be unique')  # TODO: test; display non-unique

        if self.env.python is not None and not self.env.python.is_fully_manual:
            self.python_root_modules = self._python_root_modules()
            # Root modules (or single main script as a common special case) are automatically added to input files list,
            # because they will not be present in explored local modules. Modules defined by names are library modules
            # (as implied by `-m` use case), so we don't add them to input files.
            self.inputs = list(self.inputs) + [
                VariablePath(module.path) for module in self.python_root_modules if not module.is_name
            ]

    @property
    def vars(self) -> List[str]:
        return self.__vars

    def _python_root_modules(self) -> List[PythonModule]:
        # Usually main module is derived from `cmd` automatically. First argument of `cmd` can be path to python
        # interpreter or path to main module itself in case of using shebang in it.
        #
        # For complex cases, additional root modules can be defined by user in config. Additional root modules are then
        # merged with automatically defined main module. Such merge is convenient such cases as
        # `python -m deepseed main.py` – user script is `main.py`, and `deepseed` is library module, path to which user
        # don't know.
        main_module = parse_python_main_module(self.cmd)
        if main_module:
            logger.debug('`%s` is detected as Python main module', main_module.path)
        root_modules = {main_module} if main_module else set()
        if self.env.python.root_modules_paths:
            root_modules |= {PythonModule(path) for path in self.env.python.root_modules_paths}
        if len(root_modules) == 0:
            raise ValueError('Python root module(-s) was not found automatically or set in config')
        return list(sorted(root_modules, key=lambda m: m.path))  # sort for determinism in tests

    # TODO: get rid of circular dependency `config <-> pyenv` (had to skip arg typing because of that)
    def get_job_params(self, py_env, local_modules: List[jobs.File]) -> jobs.JobParameters:
        env = jobs.Environment(
            vars=self.env.vars,
            python_env=jobs.PythonEnv(
                conda_yaml=py_env.conda_yaml,  # TODO: python: `local-project` support
                local_modules=local_modules,
            ) if py_env else None
        )
        docker_image = self.env.docker_image
        if docker_image:
            if isinstance(docker_image, str):
                env.docker_image_resource_id = docker_image
            else:
                env.docker_image_spec.CopyFrom(docker_image.proto)

        return jobs.JobParameters(
            input_files=[f.get_file() for f in self.inputs],
            output_files=[f.file_desc for f in self.outputs],
            s3_mount_ids=[p.path for p in self.s3_mounts],
            dataset_ids=[p.path for p in self.datasets],
            cmd=self.cmd,
            env=env,
            attach_project_disk=self.attach_project_disk,
            cloud_instance_type=jobs.CloudInstanceType(name=self.cloud_instance_type),
            extended_working_storage=self.working_storage
        )


PathValidatorType = Callable[[VariablePath], str]


def parse_variable_path_list(
        config: dict,
        key: str,
        validator: Optional[PathValidatorType] = None,
) -> List[VariablePath]:
    value_list = config.get(key, [])
    if not isinstance(value_list, list):
        raise ValueError(f'`{key}` should be a list')
    result = []
    for value in value_list:
        try:
            result.append(get_variable_path(value, validator))
        except ValueError as e:
            raise ValueError(f'invalid `{key}` entry: `{value}`: {e}')
    return result


VariablePathType = Union[str, Dict[str, str], Dict[str, Dict[str, str]]]

var_pattern = compile(r'[0-9a-z-A-z\-_]{1,50}')
ds_project_home = 'DS_PROJECT_HOME'
py_script_path = 'PY_SCRIPT'
reserved_vars = {ds_project_home}
local_module_prefix = '_LOCAL_MODULE'  # not reserved since such name is invalid by pattern


def get_variable_path(
        value: VariablePathType,
        validator: Optional[PathValidatorType] = None,
) -> VariablePath:
    result = parse_variable_path(value)
    if result.var and not var_pattern.fullmatch(result.var):
        raise ValueError(f'var `{result.var}` does not fit regexp {var_pattern.pattern}')
    if result.var in reserved_vars:
        raise ValueError(f'name `{result.var}` is reserved and cannot be used for variable')
    path_err = validator(result)
    if path_err:
        raise ValueError(f'value is incorrect: {path_err}')
    return result


def parse_variable_path(path: VariablePathType) -> VariablePath:
    if isinstance(path, str):
        return VariablePath(path=path)
    elif isinstance(path, dict):
        if len(path) != 1:
            raise ValueError('multiple items in dict')
        k = next(iter(path))
        v = path[k]
        if isinstance(v, str):
            return VariablePath(path=k, var=v)
        elif isinstance(v, dict):
            if list(v.keys()) != ['var']:
                raise ValueError('only `var` param is supported')
            return VariablePath(path=k, var=v['var'])
        else:
            raise ValueError('invalid dict value')
    else:
        raise ValueError('not a string or dict')


def parse_docker_image(env: dict) -> Optional[Union[str, DockerImage]]:
    if 'docker' not in env:
        return None
    docker = env['docker']
    if isinstance(docker, str):
        return docker
    elif isinstance(docker, dict):
        url = docker['image']
        username = docker.get('username')
        password_data = docker.get('password')
        password = None
        if password_data:
            if isinstance(password_data, dict) and 'secret-id' in password_data:
                password = Password(password_data['secret-id'], is_secret=True)
            elif isinstance(password_data, str):
                logger.warning(
                    'It is strongly recommended to use DataSphere secrets instead of plain passwords. '
                    'See https://cloud.yandex.ru/ru/docs/datasphere/concepts/jobs/#config'
                )
                password = Password(password_data, is_secret=False)
            else:
                raise ValueError(f'unexpected value for docker password: {password_data}')
        return DockerImage(url, username, password)
    else:
        raise ValueError(f'invalid docker image format: {docker}')


python_version_pattern = compile(r'3\.\d+(\.\d+)?')


class PythonEnvTypes(enum.Enum):
    AUTO = 'auto'
    MANUAL = 'manual'

    @classmethod
    def list(cls) -> List[str]:
        return [x.value for x in cls]


def parse_python_env(env: dict) -> Optional[PythonEnv]:
    if 'python' not in env:
        return None
    python = env['python']
    if isinstance(python, str):
        return _parse_python_env_str(python)
    elif isinstance(python, dict):
        return _parse_python_env_dict(python)
    else:
        raise ValueError(f'invalid python env format: {python}')


def _parse_python_env_str(python: str) -> PythonEnv:
    python = python.lower()
    # TODO: `python: local-project` for local code only sync
    if python != 'auto':
        raise ValueError(f'invalid python env format: {python}')
    return PythonEnv()


def _is_list_of_strings(o: Any) -> bool:
    return isinstance(o, list) and all(isinstance(e, str) for e in o)


def _parse_python_env_dict(python: dict) -> PythonEnv:
    if 'type' not in python:
        raise ValueError('you have to specify `type` of python env')
    typ = python['type']
    if typ not in PythonEnvTypes.list():
        raise ValueError(f'possible python env types are: {PythonEnvTypes.list()}')
    if typ == PythonEnvTypes.AUTO.value:
        version = None
        requirements = None
        root_modules_paths = python.get('root-paths')
        local_modules_paths = None
        pip_options = None
        if 'pip' in python:
            pip_options = PythonEnv.PipOptions()
            if 'extra-index-urls' in python['pip']:
                if not _is_list_of_strings(python['pip']['extra-index-urls']):
                    raise ValueError('`extra-index-urls` should be a list of strings')
                pip_options.extra_index_urls = python['pip']['extra-index-urls']
            if 'trusted-hosts' in python['pip']:
                if not _is_list_of_strings(python['pip']['trusted-hosts']):
                    raise ValueError('`trusted-hosts` should be a list of strings')
                pip_options.trusted_hosts = python['pip']['trusted-hosts']
            if 'no-deps' in python['pip']:
                pip_options.no_deps = python['pip']['no-deps'] == 'true'
    else:
        version = python.get('version')
        if version:
            if not isinstance(version, str) or not python_version_pattern.fullmatch(version):
                raise ValueError(f'unsupported python version: {version}')
        requirements = python.get('requirements-file')
        if requirements:
            requirements = Path(requirements)
            if not requirements.exists():
                raise ValueError(f'requirements file `{requirements}` was not found')
        root_modules_paths = python.get('root-paths')
        local_modules_paths = python.get('local-paths')
        if root_modules_paths:
            if not isinstance(root_modules_paths, list):
                raise ValueError('`root-paths` should be a list')
            if local_modules_paths:
                raise ValueError('only one of options `root-modules`, `local-paths` can be set at a time')
        if local_modules_paths:
            if not isinstance(local_modules_paths, list):
                raise ValueError('`local-paths` should be a list')
        # TODO: we can support `pip` options here to merge it with options in requirements.txt, but it will
        #  require change of server API (python env as some objects/files, not as conda.yaml string body)
        pip_options = None
    return PythonEnv(version, requirements, root_modules_paths, local_modules_paths, pip_options)


def parse_env_vars(env: dict) -> Optional[Dict[str, str]]:
    if 'vars' not in env:
        return None
    env_vars = env['vars']
    if env_vars is None:
        return None
    # Two options to specify env vars.
    #
    # env:
    #   vars:
    #     - FOO  # copy local env variable FOO
    #     - BAZ: value
    #
    # env:
    #   vars:  # deprecated option
    #     FOO: bar
    #     BAZ: value
    if isinstance(env_vars, list):
        result = {}
        for v in env_vars:
            if isinstance(v, str):
                if v not in os.environ:
                    raise ValueError(f'environment var `{v}` is missing')
                else:
                    result[v] = os.environ[v]
            elif isinstance(v, dict):
                name = list(v.keys())[0]
                value = v[name]
                if not isinstance(name, str) or not isinstance(value, str):
                    raise ValueError('environment var name and value should be str')
                result[name] = value
            else:
                raise ValueError('environment var should be specified as `- NAME` or `- NAME: VALUE`')
        return result
    elif (not isinstance(env_vars, dict) or any(
            not isinstance(x, str)
            for x in list(env_vars.keys()) + list(env_vars.values())
    )):
        raise ValueError('environment vars should be a list')  # do not tell about deprecated option
    else:
        return env_vars


def parse_env(env: Optional[dict]) -> Environment:
    if env is None:
        return Environment(vars=None, docker_image=None, python=None)
    return Environment(parse_env_vars(env), parse_docker_image(env), parse_python_env(env))


def validate_path(v: VariablePath, is_input: bool) -> str:
    p = Path(v.path)
    if is_input and not p.exists():
        return f'no such path: {p}'
    if is_input and p.is_dir():
        return f'{p} is a directory'
    is_relative = not p.is_absolute() and '..' not in p.as_posix()
    if not v.var and not is_relative:
        return f'path without variable should be relative: {p}'
    return ''


validate_input_path = partial(validate_path, is_input=True)
validate_output_path = partial(validate_path, is_input=False)

resource_id_pattern = compile(r'[0-9a-z]{20}')


def is_resource_id(s: str) -> bool:
    return isinstance(s, str) and resource_id_pattern.fullmatch(s)


def validate_resource_id(v: VariablePath) -> str:
    if not is_resource_id(v.path):
        return f'invalid resource ID: {v.path}'
    return ''


def get_resource_id(s: str, err_msg: str) -> str:
    err = validate_resource_id(VariablePath(path=s))
    if err:
        raise ValueError(f'{err_msg}: {err}')
    return s


def parse_working_storage(config: dict) -> Optional[jobs.ExtendedWorkingStorage]:
    if 'working-storage' not in config:
        return None
    ws: dict = config['working-storage']

    typ = ws.get('type', 'SSD')
    if typ != 'SSD':
        raise ValueError('possible working storage types are: [SSD]')

    if 'size' not in ws:
        raise ValueError('working storage size is not set')
    size = parse_human_size(ws['size'])
    size_gb = size >> 30
    if size % (1 << 30) != 0:
        size_gb += 1
    if size_gb < 100:
        raise ValueError('working storage size should not be less then 100 Gb')

    return jobs.ExtendedWorkingStorage(type=jobs.ExtendedWorkingStorage.StorageType.SSD, size_gb=size_gb)


# may be use string.Template for that
var_tpl_pattern = compile(r'\$\{(.+?)}')


def _to_var_reference(var: str) -> str:
    return f'${{{var}}}'


def process_cmd(config: Config) -> str:
    raw_cmd = config.cmd
    if len(raw_cmd) == 0:
        raise ValueError('empty `cmd`')
    var_to_resource_id = {x.var: x.path for x in (config.s3_mounts + config.datasets)}
    cmd = raw_cmd
    for var in var_tpl_pattern.findall(cmd):
        if var in reserved_vars:
            continue
        if var not in config.vars:
            raise ValueError(f'`cmd` contains variable not presented in config: {var}')
        if var in var_to_resource_id:
            cmd = cmd.replace(_to_var_reference(var), _to_var_reference(var_to_resource_id[var]))
    if not config.attach_project_disk and ('${%s}' % ds_project_home) in raw_cmd:
        raise ValueError(f'{ds_project_home} is unavailable since you did not add `attach-project-disk` option')
    return cmd


def parse_config(f: Union[Path, TextIO]) -> Config:
    if isinstance(f, Path):
        config_str = f.read_text()
    else:
        config_str = f.read()
    config_dict = yaml.load(StringIO(config_str), Loader=yaml.BaseLoader)
    if config_dict is None or len(config_dict) == 0:
        raise ValueError('config is empty')
    for opt in ('cmd',):
        if opt not in config_dict:
            raise ValueError(f'`{opt}` is required')
    flags = config_dict.get('flags', [])
    if not isinstance(flags, list):
        raise ValueError('`flags` should be a list')
    config = Config(
        name=config_dict.get('name'),
        desc=config_dict.get('desc'),
        cmd=config_dict['cmd'],
        inputs=parse_variable_path_list(config_dict, 'inputs', validate_input_path),
        outputs=parse_variable_path_list(config_dict, 'outputs', validate_output_path),
        s3_mounts=parse_variable_path_list(config_dict, 's3-mounts', validate_resource_id),
        datasets=parse_variable_path_list(config_dict, 'datasets', validate_resource_id),
        env=parse_env(config_dict.get('env')),
        cloud_instance_type=config_dict.get('cloud-instance-type', 'c1.4'),
        attach_project_disk='attach-project-disk' in flags,
        content=config_str,
        working_storage=parse_working_storage(config_dict)
    )
    config.cmd = process_cmd(config).strip()
    return config


UPLOAD_FILE_MAX_SIZE_BYTES = 5 * (1 << 30)  # 5Gb
UPLOAD_FILES_MAX_TOTAL_SIZE_BYTES = 10 * (1 << 30)  # 10Gb
FILES_LIST_MAX_SIZE = 100


def check_limits(config: Config, local_modules: List[jobs.File]):
    upload_files_size_bytes = 0
    for f in [path.get_file() for path in config.inputs] + local_modules:
        if f.size_bytes > UPLOAD_FILE_MAX_SIZE_BYTES:
            raise ValueError(
                f'size of file {f.desc.path} = {humanize_bytes_size(f.size_bytes)}, '
                f'while limit = {humanize_bytes_size(UPLOAD_FILE_MAX_SIZE_BYTES)}'
            )
        upload_files_size_bytes += f.size_bytes

    local_modules_msg = ' and Python local modules' if len(local_modules) else ''
    if upload_files_size_bytes > UPLOAD_FILES_MAX_TOTAL_SIZE_BYTES:
        raise ValueError(
            f'total size of input files{local_modules_msg} = {humanize_bytes_size(upload_files_size_bytes)}, '
            f'while limit = {humanize_bytes_size(UPLOAD_FILES_MAX_TOTAL_SIZE_BYTES)} bytes.'
        )
    for entries, name in (
            (config.inputs, 'input files'),
            (config.outputs, 'output files'),
            (config.s3_mounts, 's3 mounts'),
            (config.datasets, 'datasets'),
    ):
        if len(entries) > FILES_LIST_MAX_SIZE:
            raise ValueError(f'number of {name} must be not greater than {FILES_LIST_MAX_SIZE}')
