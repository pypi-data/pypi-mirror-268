from re import escape

from unittest.mock import call
from pytest import fixture, raises

from datasphere.config import PythonEnv as PythonEnvConfig
from datasphere.pyenv import PythonEnv, define_py_env, _parse_requirements
from datasphere.utils import PythonModule


class TestParseRequirements:
    def test_ok(self, tmp_path):
        f = tmp_path / 'req.txt'
        f.write_text("""
        --no-deps
        --extra-index-url https://pypi.ngc.nvidia.com
        --trusted-host nvidia.com
        beautifulsoup4
        docopt == 0.6.1
        requests [security,foo] >= 2.8.1, == 2.8.* 
            """)

        assert _parse_requirements(f) == [
            '--no-deps',
            '--extra-index-url https://pypi.ngc.nvidia.com',
            '--trusted-host nvidia.com',
            'beautifulsoup4',
            'docopt == 0.6.1',
            'requests [security,foo] >= 2.8.1, == 2.8.*',
        ]

    def test_empty(self, tmp_path):
        f = tmp_path / 'req.txt'
        f.write_text(' \n  \n')

        assert _parse_requirements(f) == []

    def test_marker(self, tmp_path):
        f = tmp_path / 'req.txt'
        f.write_text('requests [security] >= 2.8.1, == 2.8.* ; python_version < "2.7"')

        with raises(ValueError, match=escape(
                'requirement markers are not supported '
                '(requests [security] >= 2.8.1, == 2.8.* ; python_version < "2.7")'
        )):
            _parse_requirements(f)

    def test_url(self, tmp_path):
        f = tmp_path / 'req.txt'
        f.write_text('urllib3 @ https://github.com/urllib3/urllib3/archive/refs/tags/1.26.8.zip')

        with raises(ValueError, match=escape(
                'requirement url is not supported '
                '(urllib3 @ https://github.com/urllib3/urllib3/archive/refs/tags/1.26.8.zip)'
        )):
            _parse_requirements(f)

    def test_unsupported_entries(self, tmp_path):
        for entry in (
                '-r other-requirements.txt',
                './downloads/numpy-1.9.2-cp34-none-win32.whl',
                'http://wxpython.org/Phoenix/snapshot-builds/wxPython_Phoenix-3.0.3.dev1820+49a8884-cp34-none-win_amd64.whl',
        ):
            f = tmp_path / 'req.txt'
            f.write_text(entry)
            with raises(Exception):
                _parse_requirements(f)


def test_generate_conda_yaml():
    assert PythonEnv(
        version='3.10.5',
        local_modules_paths=[],
        requirements=[
            'pandas',
            'requests[foo,security]==2.8.*,>=2.8.1',
            'tensorflow==1.12.0'
        ],
        pip_options=PythonEnvConfig.PipOptions(
            extra_index_urls=['https://pypi.yandex-team.ru/simple', 'https://pypi.ngc.nvidia.com'],
            trusted_hosts=['yandex-team.ru', 'nvidia.com'],
            no_deps=True,
        )
    ).conda_yaml == (
               'name: default\n'
               'dependencies:\n'
               '- python==3.10.5\n'
               '- pip\n'
               '- pip:\n'
               '  - --no-deps\n'
               '  - --trusted-host yandex-team.ru\n'
               '  - --trusted-host nvidia.com\n'
               '  - --extra-index-url https://pypi.yandex-team.ru/simple\n'
               '  - --extra-index-url https://pypi.ngc.nvidia.com\n'
               '  - pandas\n'
               '  - requests[foo,security]==2.8.*,>=2.8.1\n'
               '  - tensorflow==1.12.0\n'
           )

    assert PythonEnv(
        version='3.10.5',
        local_modules_paths=[],
        requirements=[],
    ).conda_yaml == (
        'name: default\n'
        'dependencies:\n'
        '- python==3.10.5\n'
        '- pip\n'
    )


@fixture
def main_module():
    return PythonModule(path='main.py')


@fixture
def other_module():
    return PythonModule(path='other.py')


@fixture
def main_namespace():
    return {'foo': 'bar'}


@fixture
def other_namespace():
    return {'foo': 'baz', 'qwerty': 123}


@fixture
def get_module_namespace_mock(mocker, main_namespace, other_namespace):
    get_module_namespace = mocker.patch('datasphere.pyenv._get_module_namespace')
    get_module_namespace.side_effect = [main_namespace, other_namespace]
    return get_module_namespace


@fixture
def auto_explorer_mock(mocker):
    auto_explorer = mocker.patch('datasphere.pyenv.AutoExplorer')()
    auto_explorer.target_python = (3, 11)
    # Local modules and PyPI packages are selected in the way to also check merge functionality.
    auto_explorer.get_local_module_paths.side_effect = [
        ['lib.py'], ['submodule/utils.py', 'lib.py']
    ]
    auto_explorer.get_pypi_packages.side_effect = [
        {'tensorflow-macos': '', 'pandas': '2.0'},
        {'pandas': '2.0', 'deepseed': '0.13.0'},
    ]
    return auto_explorer


def assert_mocks_calls(get_module_namespace, auto_explorer, root_modules, namespaces, has_calls: bool = True):
    if has_calls:
        get_module_namespace.assert_has_calls([call(module) for module in root_modules])
        auto_explorer.get_local_module_paths.assert_has_calls([call(ns) for ns in namespaces])
        auto_explorer.get_pypi_packages.assert_has_calls([call(ns) for ns in namespaces])
    else:
        get_module_namespace.assert_not_called()
        auto_explorer.get_local_module_paths.assert_not_called()
        auto_explorer.get_pypi_packages.assert_not_called()


def test_define_auto_py_env(get_module_namespace_mock, auto_explorer_mock, main_module, main_namespace):
    py_env = define_py_env([main_module], PythonEnvConfig())

    assert_mocks_calls(get_module_namespace_mock, auto_explorer_mock, [main_module], [main_namespace])

    assert py_env == PythonEnv(
        version='3.11',
        local_modules_paths=['lib.py'],
        requirements=['pandas==2.0', 'tensorflow-macos'],
    )


def test_define_partially_manual_py_env(get_module_namespace_mock, auto_explorer_mock, main_module, main_namespace, tmp_path):
    req = tmp_path / 'req.txt'
    req.write_text("""
--no-deps
tensorflow >= 1.12.0
pandas
    """)

    py_env = define_py_env([main_module], PythonEnvConfig('3.10.5', req))

    assert_mocks_calls(get_module_namespace_mock, auto_explorer_mock, [main_module], [main_namespace])

    assert py_env == PythonEnv(
        version='3.10.5',
        local_modules_paths=['lib.py'],
        requirements=['--no-deps', 'tensorflow >= 1.12.0', 'pandas'],
    )


def test_define_fully_manual_py_env(get_module_namespace_mock, auto_explorer_mock, tmp_path):
    req = tmp_path / 'req.txt'
    req.write_text("""
--extra-index-url https://pypi.ngc.nvidia.com 
--trusted-host nvidia.com
tensorflow >= 1.12.0
pandas
    """)

    py_env = define_py_env([], PythonEnvConfig('3.10.5', req, [], ['utils.py']))

    assert_mocks_calls(get_module_namespace_mock, auto_explorer_mock, None, None, has_calls=False)

    assert py_env == PythonEnv(
        version='3.10.5',
        local_modules_paths=['utils.py'],
        requirements=['--extra-index-url https://pypi.ngc.nvidia.com', '--trusted-host nvidia.com', 'tensorflow >= 1.12.0', 'pandas'],
    )


def test_define_auto_py_env_on_multiple_root_modules(get_module_namespace_mock, auto_explorer_mock, main_module, other_module, main_namespace, other_namespace, tmp_path):
    py_env = define_py_env([main_module, other_module], PythonEnvConfig())

    assert_mocks_calls(get_module_namespace_mock, auto_explorer_mock, [main_module, other_module], [main_namespace, other_namespace])

    assert py_env == PythonEnv(
        version='3.11',
        local_modules_paths=['lib.py', 'submodule/utils.py'],
        requirements=['deepseed==0.13.0', 'pandas==2.0', 'tensorflow-macos'],
    )
