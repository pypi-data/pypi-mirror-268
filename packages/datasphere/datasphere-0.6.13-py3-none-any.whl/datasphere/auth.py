from datetime import datetime, timedelta
import logging
import os
import subprocess
from typing import List, Optional, Tuple

import grpc

from datasphere.api import env, ServerEnv, iam_endpoint
from datasphere.version import version
from yandex.cloud.iam.v1.iam_token_service_pb2 import CreateIamTokenRequest
from yandex.cloud.iam.v1.iam_token_service_pb2_grpc import IamTokenServiceStub

logger = logging.getLogger(__name__)

oauth_token_env_var_1 = 'YC_TOKEN'  # As in `yc`
oauth_token_env_var_2 = 'YC_OAUTH_TOKEN'  # More consistent with IAM token env var
# Announced in https://bb.yandexcloud.net/projects/CLOUD/repos/cloud-go/browse/cli/CHANGELOG.md
iam_token_env_var = 'YC_IAM_TOKEN'


def create_iam_token(oauth_token: Optional[str]) -> str:
    if oauth_token:
        return create_iam_token_by_oauth_token(oauth_token)

    # If user does not provide OAuth token, or OAuth token is not applicable (i.e. for YC staff with federations),
    # we consider that `yc` CLI is installed and configured properly (either on prod or preprod installation).
    return create_iam_token_with_yc()


def create_iam_token_by_oauth_token(oauth_token: str) -> str:
    logger.debug('creating iam token using oauth token ...')
    stub = IamTokenServiceStub(grpc.secure_channel(iam_endpoint, grpc.ssl_channel_credentials()))
    req = CreateIamTokenRequest(yandex_passport_oauth_token=oauth_token)
    resp = stub.Create(req)
    return resp.iam_token


def create_iam_token_with_yc() -> str:
    env_token: Optional[str] = os.environ.get(iam_token_env_var)
    if env_token:
        logger.warning('iam token from env var is not refreshable, so it may expire over time')
        return env_token
    logger.debug('oauth token is not provided, creating iam token through `yc` ...')
    try:
        # TODO: capture stderr, process return code
        process = subprocess.run(
            ['yc', 'iam', 'create-token', '--no-user-output'],
            stdout=subprocess.PIPE, universal_newlines=True,
        )
    except FileNotFoundError:
        raise RuntimeError('You have not provided OAuth token. You have to install Yandex Cloud CLI '
                           '(https://cloud.yandex.com/docs/cli/) to authenticate automatically.')

    # There may be another output before the token, for example, info about opening the browser.
    # TODO: not sure if token will be last line (update suggestion appears regardless of --no-user-output flag
    return process.stdout.strip().split('\n')[-1]


iam_token_refresh_period = timedelta(hours=1)  # 12h is maximum for IAM token
iam_token_refreshed_at: Optional[datetime] = None
current_iam_token: Optional[str] = None


def get_md(oauth_token: Optional[str]) -> List[Tuple[str, str]]:
    metadata = [("x-client-version", f"datasphere={version}")]

    if env == ServerEnv.DEV:
        return metadata

    global current_iam_token
    global iam_token_refreshed_at
    now = datetime.now()

    iam_token_expired = iam_token_refreshed_at is None or now - iam_token_refreshed_at > iam_token_refresh_period
    if iam_token_expired:
        current_iam_token = create_iam_token(oauth_token)
        iam_token_refreshed_at = now

    assert current_iam_token

    metadata.append(('authorization', f'Bearer {current_iam_token}'))

    return metadata
