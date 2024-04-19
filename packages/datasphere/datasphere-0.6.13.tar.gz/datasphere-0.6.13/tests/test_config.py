from pathlib import Path
import re
import sys
from typing import List, Optional

from envzy import ModulePathsList
from pytest import raises, fixture

import datasphere.config
from datasphere.config import (
    validate_resource_id,
    validate_path,
    validate_input_path,
    parse_variable_path,
    VariablePath,
    get_variable_path,
    parse_variable_path_list,
    DockerImage,
    Password,
    parse_docker_image,
    PythonEnv,
    parse_python_env,
    Environment,
    parse_env,
    process_cmd,
    Config,
    parse_config,
    check_limits,
    parse_working_storage,
    parse_env_vars
)
from datasphere.api import jobs_pb2 as jobs
from datasphere.utils import PythonModule


@fixture
def input_file():
    path = Path('input.txt')
    path.write_text('foo')
    yield str(path)
    path.unlink()


def test_validate_resource_id():
    assert validate_resource_id(VariablePath(path='foo')) == 'invalid resource ID: foo'
    assert validate_resource_id(VariablePath(path='bt10gr4c1b081bidoses')) == ''


def test_validate_path(tmp_path, input_file):
    assert validate_path(VariablePath(path='foobar.pdf'), is_input=True) == 'no such path: foobar.pdf'
    cur_dir = str(Path(__file__).parent.absolute())
    assert validate_path(VariablePath(path=cur_dir), is_input=True) == f'{cur_dir} is a directory'
    assert validate_path(VariablePath(path='../setup.py'), is_input=False) == \
           'path without variable should be relative: ../setup.py'

    f = tmp_path / 'foo.txt'
    f.write_text('bar')
    assert validate_path(VariablePath(path=str(f.absolute())), is_input=True) == \
           f'path without variable should be relative: {f.absolute()}'

    assert validate_path(VariablePath(path='foobar.pdf'), is_input=False) == ''
    assert validate_path(VariablePath(path=input_file), is_input=True) == ''
    assert validate_path(VariablePath(path=str(f.absolute()), var='PARAMS'), is_input=True) == ''


def test_parse_variable_value():
    assert parse_variable_path('misc/logging.yaml') == VariablePath('misc/logging.yaml')
    assert parse_variable_path({'data/model.bin': 'MODEL'}) == VariablePath('data/model.bin', 'MODEL')
    assert parse_variable_path(
        {'/usr/share/params.json': {'var': 'PARAMS'}}
    ) == VariablePath('/usr/share/params.json', 'PARAMS')

    with raises(ValueError, match='not a string or dict'):
        parse_variable_path(42)  # noqa

    with raises(ValueError, match='multiple items in dict'):
        parse_variable_path({'data/model.bin': '', 'var': 'MODEL'})

    with raises(ValueError, match='only `var` param is supported'):
        parse_variable_path({'/usr/share/params.json': {'foo': 'bar'}})

    with raises(ValueError, match='invalid dict value'):
        parse_variable_path({'/usr/share/params.json': 42})  # noqa


def test_get_variable_value():
    with raises(ValueError, match='var `!foo.j` does not fit regexp [0-9a-z-A-z\\-_]{1,50}'):
        get_variable_path({'/usr/share/params.json': {'var': '!foo.j'}})

    with raises(ValueError, match='value is incorrect: invalid resource ID: foo'):
        get_variable_path('foo', validate_resource_id)

    with raises(ValueError, match='name `DS_PROJECT_HOME` is reserved and cannot be used for variable'):
        get_variable_path({'data/model.bin': 'DS_PROJECT_HOME'})


def test_parse_variable_value_list():
    with raises(ValueError, match='`inputs` should be a list'):
        parse_variable_path_list({'inputs': {'foo': 'bar'}}, 'inputs')

    with raises(ValueError, match='invalid `inputs` entry: `foobar.pdf`: value is incorrect: no such path: foobar.pdf'):
        parse_variable_path_list({'inputs': ['foobar.pdf']}, 'inputs', validate_input_path)


@fixture
def docker_image_with_plain_password_dict() -> dict:
    return {
        'docker': {
            'image': 'cr.yandex/crtabcdef12345678900/myenv:0.1',
            'username': 'foo',
            'password': 'bar',
        }
    }


@fixture
def docker_image_with_plain_password() -> DockerImage:
    return DockerImage(
        url='cr.yandex/crtabcdef12345678900/myenv:0.1',
        username='foo',
        password=Password(text='bar', is_secret=False),
    )


@fixture
def docker_image_with_secret_password_no_username_dict() -> dict:
    return {
        'docker': {
            'image': 'ubuntu:focal',
            'password': {'secret-id': 'CR_PASSWORD'},
        }
    }


@fixture
def docker_image_with_secret_password_no_username() -> DockerImage:
    return DockerImage(
        url='ubuntu:focal',
        username=None,
        password=Password(text='CR_PASSWORD', is_secret=True),
    )


def test_parse_docker_image(
        docker_image_with_plain_password_dict,
        docker_image_with_plain_password,
        docker_image_with_secret_password_no_username_dict,
        docker_image_with_secret_password_no_username,
):
    assert parse_docker_image({'inputs': []}) is None

    assert parse_docker_image({'docker': 'b1gldgej4sak01tcg79m'}) == 'b1gldgej4sak01tcg79m'

    assert parse_docker_image(docker_image_with_plain_password_dict) == docker_image_with_plain_password
    assert docker_image_with_plain_password.proto == jobs.DockerImageSpec(
        image_url='cr.yandex/crtabcdef12345678900/myenv:0.1',
        username='foo',
        password_plain_text='bar',
    )

    assert parse_docker_image(docker_image_with_secret_password_no_username_dict) == \
           docker_image_with_secret_password_no_username
    assert docker_image_with_secret_password_no_username.proto == jobs.DockerImageSpec(
        image_url='ubuntu:focal',
        username=None,
        password_ds_secret_name='CR_PASSWORD',
    )

    with raises(ValueError, match="unexpected value for docker password: {'secret': 'CR_PASSWORD'}"):
        parse_docker_image({'docker': {
            'image': 'ubuntu:focal',
            'password': {'secret': 'CR_PASSWORD'},
        }})

    with raises(ValueError, match='unexpected value for docker password: 12345'):
        parse_docker_image({'docker': {
            'image': 'ubuntu:focal',
            'password': 12345,
        }})


@fixture
def requirements_file(tmp_path) -> Path:
    f = tmp_path / 'requirements.txt'
    f.write_text('')
    return f


def test_parse_python_env(requirements_file):
    for env_dict, expected_env, err in (
            ({}, None, None),
            ({'python': 'auto'}, PythonEnv(), None),
            ({'python': 'foo'}, None, 'invalid python env format: foo'),
            ({'python': 42}, None, 'invalid python env format: 42'),
            ({'python': {}}, None, 'you have to specify `type` of python env'),
            ({'python': {'type': 'foo'}}, None, re.escape("possible python env types are: ['auto', 'manual']")),
            ({'python': {'type': 'manual', 'version': '3.10.5'}}, PythonEnv(version='3.10.5'), None),
            ({'python': {'type': 'manual', 'requirements-file': requirements_file}}, PythonEnv(requirements=requirements_file), None),
            ({'python': {'type': 'manual', 'version': '3.9', 'requirements-file': requirements_file, 'local-paths': ['utils.py']}}, PythonEnv(version='3.9', requirements=requirements_file, local_modules_paths=['utils.py']), None),
            ({'python': {'type': 'manual', 'version': '3.11.a'}}, None, 'unsupported python version: 3.11.a'),
            ({'python': {'type': 'manual', 'version': '2.7'}}, None, 'unsupported python version: 2.7'),
            ({'python': {'type': 'manual', 'requirements-file': 'not-existent.txt'}}, None, 'requirements file `not-existent.txt` was not found'),
            ({'python': {'type': 'manual', 'local-paths': 'utils.py'}}, None, '`local-paths` should be a list'),
            ({'python': {'type': 'manual', 'root-paths': 'utils.py'}}, None, '`root-paths` should be a list'),
            ({'python': {'type': 'manual', 'root-paths': ['other.py'], 'local-paths': ['utils.py']}}, None, 'only one of options `root-modules`, `local-paths` can be set at a time'),
            ({'python': {'type': 'auto'}}, PythonEnv(), None),
            ({'python': {'type': 'auto', 'pip': {}}}, PythonEnv(pip_options=PythonEnv.PipOptions()), None),
            ({'python': {'type': 'auto', 'pip': {'extra-index-urls': 'https://example.com'}}}, None, '`extra-index-urls` should be a list of strings'),
            ({'python': {'type': 'auto', 'pip': {'extra-index-urls': ['https://pypi.yandex-team.ru/simple', 'https://pypi.ngc.nvidia.com']}}}, PythonEnv(pip_options=PythonEnv.PipOptions(extra_index_urls=['https://pypi.yandex-team.ru/simple', 'https://pypi.ngc.nvidia.com'])), None),
            ({'python': {'type': 'auto', 'pip': {'trusted-hosts': 'example.com'}}}, None, '`trusted-hosts` should be a list of strings'),
            ({'python': {'type': 'auto', 'pip': {'trusted-hosts': ['example.com', 'knownhost.com:5555']}}}, PythonEnv(pip_options=PythonEnv.PipOptions(trusted_hosts=['example.com', 'knownhost.com:5555'])), None),
            ({'python': {'type': 'auto', 'pip': {'no-deps': 'true'}}}, PythonEnv(pip_options=PythonEnv.PipOptions(no_deps=True)), None),
            ({'python': {'type': 'auto', 'pip': {'extra-index-urls': ['https://pypi.yandex-team.ru/simple', 'https://pypi.ngc.nvidia.com'], 'trusted-hosts': ['example.com', 'knownhost.com:5555']}, 'no-deps': 'nope'}}, PythonEnv(pip_options=PythonEnv.PipOptions(extra_index_urls=['https://pypi.yandex-team.ru/simple', 'https://pypi.ngc.nvidia.com'], trusted_hosts=['example.com', 'knownhost.com:5555'], no_deps=False)), None),
            ({'python': {'type': 'auto', 'root-paths': ['other.py']}}, PythonEnv(root_modules_paths=['other.py']), None),
    ):
        if err:
            with raises(ValueError, match=err):
                parse_python_env(env_dict)
        else:
            assert parse_python_env(env_dict) == expected_env


def test_parse_env_vars(mocker):
    mocker.patch.dict('os.environ', {'LOCAL_ENV_VAR': 'local_env_value'})

    for env, expected, err in (
            ({'foo': 'bar'}, None, None),
            (
                    {'vars': ['LOCAL_ENV_VAR', {'NAME': 'value'}]},
                    {'LOCAL_ENV_VAR': 'local_env_value', 'NAME': 'value'},
                    None
            ),
            ({'vars': ['MISSING']}, None, 'environment var `MISSING` is missing'),
            ({'vars': [42]}, None, 'environment var should be specified as `- NAME` or `- NAME: VALUE`'),
            ({'vars': [{'NAME': 42}]}, None, 'environment var name and value should be str'),
            ({'vars': [{42: 'VALUE'}]}, None, 'environment var name and value should be str'),
            ({'vars': {'FOO': 'bar'}}, {'FOO': 'bar'}, None),
            ({'vars': 42}, None, 'environment vars should be a list'),
            ({'vars': {'foo': 42}}, None, 'environment vars should be a list'),
            ({'vars': {42: 'foo'}}, None, 'environment vars should be a list'),
    ):
        if err:
            with raises(ValueError, match=re.escape(err)):
                parse_env_vars(env)
        else:
            assert parse_env_vars(env) == expected


def test_parse_env(
        mocker,
        docker_image_with_secret_password_no_username_dict,
        docker_image_with_secret_password_no_username,
):
    assert parse_env(None) == Environment(vars=None, docker_image=None, python=None)

    assert parse_env({
        'docker': 'b1gldgej4sak01tcg79m',
        'python': 'auto',
    }) == Environment(
        vars=None,
        docker_image='b1gldgej4sak01tcg79m',
        python=PythonEnv(),
    )

    mocker.patch.dict('os.environ', {'LOCAL_ENV_VAR': 'local_env_value'})

    assert parse_env({
        'vars': ['LOCAL_ENV_VAR', {'NAME': 'value'}],
        **docker_image_with_secret_password_no_username_dict,
    }) == Environment(
        vars={'LOCAL_ENV_VAR': 'local_env_value', 'NAME': 'value'},
        docker_image=docker_image_with_secret_password_no_username,
        python=None,
    )


def test_parse_config_errors(tmp_path):
    cfg = tmp_path / 'cfg1.yaml'
    cfg.write_text('')
    with raises(ValueError, match='config is empty'):
        parse_config(cfg.absolute())

    cfg = tmp_path / 'cfg2.yaml'
    cfg.write_text("""
name: foo
    """)
    with raises(ValueError, match='`cmd` is required'):
        parse_config(cfg.absolute())

    cfg = tmp_path / 'cfg3.yaml'
    cfg.write_text("""
cmd: python src/main.py
flags: 
  attach-project-disk: true
    """)
    with raises(ValueError, match='`flags` should be a list'):
        parse_config(cfg.absolute())

    params = tmp_path / 'params.json'
    params.write_text("{}")

    cfg = tmp_path / 'cfg4.yaml'
    cfg.write_text(f"""
cmd: python src/main.py
inputs:
  - {params.absolute()}:
      var: DATA
datasets:
  - bt12tlsc3nkt2opg2h61:
      var: DATA
    """)
    with raises(ValueError, match='variables in config should be unique'):
        parse_config(cfg.absolute())


def test_process_cmd():
    cfg = Config(
        cmd="""
python src/main.py 
  --params ${PARAMS}
  --features ${DATA}/features.tsv 
  --validate ${CIFAR}/val.json
  --normalizer ${DS_PROJECT_HOME}/misc/norm.bin
  --model ${MODEL}
  --foo ${CIFAR}/${DATA}/bar.txt
  --baz ${bt12tlsc3nkt2opg2h61}/bob.txt
  --base-var ${VAR}
  --prefixed-var ${PREFIXED_VAR}
  --postfixed-var ${VAR_POSTFIXED}
  --infixed-var ${INFIXED_VAR_INFIXED}
  --epochs 5
        """.strip(),
        inputs=[
            VariablePath(path='misc/logging.yaml'),
            VariablePath(path='/usr/share/params.json', var='PARAMS'),
        ],
        outputs=[
            VariablePath(path='data/model.bin', var='MODEL'),
            VariablePath(path='other/metrics.png'),
        ],
        s3_mounts=[],
        datasets=[
            VariablePath(path='bt12tlsc3nkt2opg2h61', var='CIFAR'),
            VariablePath(path='var', var='VAR'),
            VariablePath(path='prefixed', var='PREFIXED_VAR'),
            VariablePath(path='postfixed', var='VAR_POSTFIXED'),
            VariablePath(path='infixed', var='INFIXED_VAR_INFIXED'),
        ],
        env=Environment(vars=None, docker_image=None, python=PythonEnv()),
        cloud_instance_type='c1.4',
        attach_project_disk=False,
        content='nevermind',
    )

    with raises(ValueError, match='`cmd` contains variable not presented in config: DATA'):
        process_cmd(cfg)

    cfg.s3_mounts = [VariablePath(path='bt10gr4c1b081bidoses', var='DATA')]
    cfg.__post_init__()

    with raises(ValueError, match='DS_PROJECT_HOME is unavailable since you did not add `attach-project-disk` option'):
        process_cmd(cfg)

    cfg.attach_project_disk = True
    cmd = process_cmd(cfg)

    assert cmd == """
python src/main.py 
  --params ${PARAMS}
  --features ${bt10gr4c1b081bidoses}/features.tsv 
  --validate ${bt12tlsc3nkt2opg2h61}/val.json
  --normalizer ${DS_PROJECT_HOME}/misc/norm.bin
  --model ${MODEL}
  --foo ${bt12tlsc3nkt2opg2h61}/${bt10gr4c1b081bidoses}/bar.txt
  --baz ${bt12tlsc3nkt2opg2h61}/bob.txt
  --base-var ${var}
  --prefixed-var ${prefixed}
  --postfixed-var ${postfixed}
  --infixed-var ${infixed}
  --epochs 5
        """.strip()


def test_parse_config(
        mocker,
        tmp_path,
        docker_image_with_plain_password,
        docker_image_with_secret_password_no_username,
        input_file,
        requirements_file,
):
    params_f = tmp_path / 'params.json'
    params_f.write_text('{}')

    mocker.patch.dict('os.environ', {'PYTHONBUFFERED': 'true'})

    cfg_f = tmp_path / 'cfg1.yaml'
    cfg_f.write_text(f"""
name: my-script
desc: Learning model using PyTorch
cmd: >  # YAML multiline string
  python src/main.py 
    --params ${{PARAMS}}
    --features ${{S3}}/features.tsv
    --features ${{b3p16de49mh0f9khpar3}}/features-2.tsv
    --validate ${{CIFAR}}/val.json
    --validate ${{b3p26uhut5adiq13pmih}}/val-2.json
    --normalizer ${{DS_PROJECT_HOME}}/misc/norm.bin
    --model ${{MODEL}}
    --epochs 5
inputs:
  - {input_file}
  - {params_f.absolute()}:
      var: PARAMS
outputs:
  - data/model.bin: MODEL
  - other/metrics.png
s3-mounts:
  - b3p16de49mh0f9khpar3
  - bt10gr4c1b081bidoses:
      var: S3
datasets:
  - b3p26uhut5adiq13pmih
  - bt12tlsc3nkt2opg2h61:
      var: CIFAR
env:
  vars:
    - PYTHONBUFFERED
    - PASSWORD: qwerty
    - DEVICE_COUNT: 8
  docker: b1gldgej4sak01tcg79m
  python: auto
flags:
  - attach-project-disk
cloud-instance-type: g2.8
working-storage:
  type: SSD
  size: 123 Gb
    """.strip())
    cfg = parse_config(cfg_f.absolute())
    assert cfg == Config(
        name='my-script',
        desc='Learning model using PyTorch',
        cmd="""
python src/main.py 
  --params ${PARAMS}
  --features ${bt10gr4c1b081bidoses}/features.tsv
  --features ${b3p16de49mh0f9khpar3}/features-2.tsv
  --validate ${bt12tlsc3nkt2opg2h61}/val.json
  --validate ${b3p26uhut5adiq13pmih}/val-2.json
  --normalizer ${DS_PROJECT_HOME}/misc/norm.bin
  --model ${MODEL}
  --epochs 5
        """.strip(),
        inputs=[
            VariablePath(path=input_file),
            VariablePath(path=str(params_f.absolute()), var='PARAMS'),
        ],
        outputs=[
            VariablePath(path='data/model.bin', var='MODEL'),
            VariablePath(path='other/metrics.png'),
        ],
        s3_mounts=[
            VariablePath(path='b3p16de49mh0f9khpar3'),
            VariablePath(path='bt10gr4c1b081bidoses', var='S3'),
        ],
        datasets=[
            VariablePath(path='b3p26uhut5adiq13pmih'),
            VariablePath(path='bt12tlsc3nkt2opg2h61', var='CIFAR'),
        ],
        env=Environment(
            vars={'PYTHONBUFFERED': 'true', 'PASSWORD': 'qwerty', 'DEVICE_COUNT': '8'},
            docker_image='b1gldgej4sak01tcg79m',
            python=PythonEnv(),
        ),
        cloud_instance_type='g2.8',
        attach_project_disk=True,
        content=cfg_f.read_text(),
        working_storage=jobs.ExtendedWorkingStorage(type=jobs.ExtendedWorkingStorage.StorageType.SSD, size_gb=123)
    )

    cfg_f = tmp_path / 'cfg2.yaml'
    cfg_f.write_text("""
cmd: python run.py
env:
  vars:
    PASSWORD: qwerty
    DEVICE_COUNT: 8
  docker:
    image: cr.yandex/crtabcdef12345678900/myenv:0.1
    username: foo
    password: bar
    """.strip())
    cfg = parse_config(cfg_f.absolute())
    assert cfg == Config(
        name=None,
        desc=None,
        cmd='python run.py',
        inputs=[],
        outputs=[],
        s3_mounts=[],
        datasets=[],
        env=Environment(
            vars={'PASSWORD': 'qwerty', 'DEVICE_COUNT': '8'},
            docker_image=docker_image_with_plain_password,
            python=None,
        ),
        cloud_instance_type='c1.4',
        attach_project_disk=False,
        content=cfg_f.read_text(),
    )

    cfg_f = tmp_path / 'cfg3.yaml'
    cfg_f.write_text(f"""
name: my-script
cmd: python run.py
env:
  docker:
    image: ubuntu:focal
    password:
       secret-id: CR_PASSWORD
  python:
    type: manual
    version: 3.10.5
    requirements-file: {requirements_file}
        """.strip())
    cfg = parse_config(cfg_f.absolute())
    assert cfg == Config(
        name='my-script',
        cmd='python run.py',
        inputs=[],
        outputs=[],
        s3_mounts=[],
        datasets=[],
        env=Environment(
            vars=None,
            docker_image=docker_image_with_secret_password_no_username,
            python=PythonEnv(version='3.10.5', requirements=requirements_file),
        ),
        cloud_instance_type='c1.4',
        attach_project_disk=False,
        content=cfg_f.read_text(),
    )


@fixture
def python_symlink(tmp_path):
    link = tmp_path / 'bydhon'
    link.symlink_to(sys.executable)
    return link


def test_python_root_modules(python_symlink):
    def get_cfg(cmd: str, is_python: bool = True, root_modules_paths: Optional[ModulePathsList] = None):
        return Config(
            cmd=cmd,
            inputs=[],
            outputs=[],
            s3_mounts=[],
            datasets=[],
            env=Environment(
                vars=None,
                docker_image=None,
                python=PythonEnv(root_modules_paths=root_modules_paths) if is_python else None,
            ),
            cloud_instance_type='c1.4',
            attach_project_disk=False,
            content='nevermind',
        )

    cfg = get_cfg(cmd='python src/main.py --foo bar')
    assert cfg.python_root_modules == [PythonModule(path='src/main.py')]

    cfg = get_cfg(cmd=f'{python_symlink} -m run')
    assert cfg.python_root_modules == [PythonModule(path='run', is_name=True)]

    # Merge auto-defined library module with user-defined root module.
    cfg = get_cfg(cmd='python3 -m deepseed --epochs 5 main.py', root_modules_paths=['main.py'])
    assert cfg.python_root_modules == [PythonModule(path='deepseed', is_name=True), PythonModule(path='main.py')]

    # Drop duplicates during auto-defined and user-defined modules merge.
    cfg = get_cfg(cmd='python main.py other.py', root_modules_paths=['main.py', 'other.py'])
    assert cfg.python_root_modules == [PythonModule(path='main.py'), PythonModule(path='other.py')]

    cfg = get_cfg(cmd='ls .', is_python=False)
    assert cfg.python_root_modules == []


def test_check_limits(monkeypatch, tmp_path):
    monkeypatch.setattr(datasphere.config, 'UPLOAD_FILE_MAX_SIZE_BYTES', 600)
    monkeypatch.setattr(datasphere.config, 'UPLOAD_FILES_MAX_TOTAL_SIZE_BYTES', 2000)
    monkeypatch.setattr(datasphere.config, 'FILES_LIST_MAX_SIZE', 2)

    paths = []
    for i in range(3):
        f = tmp_path / f'{i}.txt'
        f.write_text(str(i))
        paths.append(VariablePath(str(f)))

    big_f = tmp_path / 'big.txt'
    big_f.write_bytes(b'1' * 512)
    big_path = VariablePath(str(big_f))

    huge_f = tmp_path / 'huge.txt'
    huge_f.write_bytes(b'1' * 700)
    huge_f = VariablePath(str(huge_f))

    def get_cfg(
            inputs: List[VariablePath] = None,
            outputs: List[VariablePath] = None,
            s3_mounts: List[VariablePath] = None,
            datasets: List[VariablePath] = None,
    ):
        return Config(
            cmd=f'python {paths[0].path}',
            inputs=inputs or [],
            outputs=outputs or [],
            s3_mounts=s3_mounts or [],
            datasets=datasets or [],
            env=Environment(vars=None, docker_image=None, python=PythonEnv()),
            cloud_instance_type='c1.4',
            attach_project_disk=False,
            content='nevermind',
        )

    with raises(ValueError, match=f'size of file {huge_f.path} = 700.0B, while limit = 600.0B'):
        check_limits(get_cfg(inputs=[huge_f]), [])
    with raises(ValueError, match=f'size of file {huge_f.path} = 700.0B, while limit = 600.0B'):
        check_limits(get_cfg(inputs=[]), [huge_f.get_file()])
    with raises(ValueError, match='total size of input files = 2.0KB, while limit = 2.0KB.'):
        check_limits(get_cfg(inputs=[big_path] * 4), [])
    with raises(ValueError, match='total size of input files and Python local modules = 2.5KB, while limit = 2.0KB.'):
        check_limits(get_cfg(inputs=[big_path] * 2), [big_path.get_file()] * 3)

    with raises(ValueError, match='number of input files must be not greater than 2'):
        check_limits(get_cfg(inputs=paths), [])
    with raises(ValueError, match='number of output files must be not greater than 2'):
        check_limits(get_cfg(outputs=paths), [])
    with raises(ValueError, match='number of s3 mounts must be not greater than 2'):
        check_limits(get_cfg(s3_mounts=paths), [])
    with raises(ValueError, match='number of datasets must be not greater than 2'):
        check_limits(get_cfg(datasets=paths), [])


def test_working_storage():
    def expected(size_gb: int) -> jobs.ExtendedWorkingStorage:
        return jobs.ExtendedWorkingStorage(type=jobs.ExtendedWorkingStorage.StorageType.SSD, size_gb=size_gb)

    assert parse_working_storage({}) is None

    assert parse_working_storage({'working-storage': {'size': '100Gb'}}) == expected(100)
    assert parse_working_storage({'working-storage': {'size': '100 Gb'}}) == expected(100)
    assert parse_working_storage({'working-storage': {'size': '107374182000'}}) == expected(100)
    assert parse_working_storage({'working-storage': {'size': '1TB'}}) == expected(1024)

    with raises(ValueError, match='possible working storage types are: \[SSD\]'):
        parse_working_storage({'working-storage': {'type': 'HDD', 'size': '123'}})

    with raises(ValueError, match='working storage size is not set'):
        parse_working_storage({'working-storage': {'type': 'SSD'}})

    with raises(ValueError, match='working storage size should not be less then 100 Gb'):
        parse_working_storage({'working-storage': {'type': 'SSD', 'size': '123'}})
