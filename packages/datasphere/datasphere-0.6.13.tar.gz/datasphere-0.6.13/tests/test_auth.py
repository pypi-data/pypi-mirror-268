from datetime import timedelta
from unittest.mock import Mock, call
import re

import pytest

from datasphere.auth import create_iam_token, get_md
from yandex.cloud.iam.v1.iam_token_service_pb2 import CreateIamTokenRequest, CreateIamTokenResponse


def test_create_iam_token_with_sdk(mocker):
    def Create(req: CreateIamTokenRequest):  # noqa
        return CreateIamTokenResponse(iam_token=f'iam token for oauth token {req.yandex_passport_oauth_token}')

    stub = mocker.patch('datasphere.auth.IamTokenServiceStub')()
    stub.Create = Create

    assert create_iam_token('AQAD***') == 'iam token for oauth token AQAD***'


def test_create_iam_token_with_yc(mocker):
    yc_process = Mock()
    yc_process.stdout = """

You are going to be authenticated via federation-id 'team.example.federation'.
Your federation authentication web site will be opened.
After your successful authentication, you will be redirected to cloud console'.

Press 'enter' to continue...
t1.9eudm***
    """

    mocker.patch('subprocess.run', return_value=yc_process)

    assert create_iam_token(None) == 't1.9eudm***'


def test_get_iam_token_from_env(mocker):
    mocker.patch.dict('os.environ', {'YC_IAM_TOKEN': 'iam token'})
    assert create_iam_token(None) == 'iam token'


def test_error_no_yc(mocker):
    mocker.patch('subprocess.run', side_effect=FileNotFoundError)

    with pytest.raises(RuntimeError, match=re.escape(
            'You have not provided OAuth token. You have to install Yandex Cloud CLI '
            '(https://cloud.yandex.com/docs/cli/) to authenticate automatically.'
    )):
        create_iam_token(None)


def test_iam_token_refresh(mocker):
    oauth_token = 'AQAD***'

    iam_tokens = ['iam_token_1', 'iam_token_2']
    iam_tokens_md = [('authorization', f'Bearer {iam_token}') for iam_token in iam_tokens]

    create_iam_token_stub = mocker.patch('datasphere.auth.create_iam_token')
    create_iam_token_stub.return_value = iam_tokens[0]

    md1 = get_md(oauth_token)
    md2 = get_md(oauth_token)

    create_iam_token_stub.assert_called_once_with(oauth_token)
    assert iam_tokens_md[0] in md1
    assert iam_tokens_md[0] in md2

    create_iam_token_stub.return_value = iam_tokens[1]

    iam_token_refresh_period = mocker.patch('datasphere.auth.iam_token_refresh_period')
    iam_token_refresh_period.__lt__.return_value = True

    md3 = get_md(oauth_token)

    create_iam_token_stub.assert_has_calls([call(oauth_token), call(oauth_token)])

    assert iam_tokens_md[1] in md3
