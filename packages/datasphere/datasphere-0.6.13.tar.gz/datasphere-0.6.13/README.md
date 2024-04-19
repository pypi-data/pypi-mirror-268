- Setup
  - Run `scripts/install.sh`, it will:
    - Pull `.proto` files and generate descriptors,
    - Install this package in editable mode in active venv.
    - Add flag `--priv` to script to generate private protobuf. 
  - Install venv with requirements from `setup.py`.
- Unit tests
  - Use `tox` to run tests on all available Python versions. 
  - Tests are in `tests/` directory.
  - Use `pytest-recording` and `pytest --block-network` to block potential network requests in tests.
- E2E tests
  - In these tests we launch client on real server and check expected results.
  - `cd tests_e2e/`.
  - Create venv installing this package as editable (`pip install -e ..`). Further steps are performed in this venv.
  - If you run Python program, install additional pip libraries which your script uses (i.e. `pip install pandas`).
  - Further steps depends on server environment. Possible cases are:
    - `DEV` environment – we use launched locally DataSphere services, or simple server mock, written in Python here in 
      this repo.
      - To run server mock, see `python servermock/main.py --help` to see how to launch server. You will have to specify
      - S3 storage data to generate presigned URLs for client.
      - Note: server mock is currently not up to date.
    - `PREPROD` environment – we use DataSphere preprod server.
      - Define path to YandexInternalCA with env variable `ROOT_CA` (see https://wiki.yandex-team.ru/security/ssl/sslclientfix).
      - Use some real project ID, i.e. `b3pbocd5dua07ojecibq`.
    - `PREPROD_NO_GW` environment – same as `PREPROD`, except that client will connect to lobby host directly
      bypassing gateway.
  - Now, you can run tests using two different ways:
    - _Debug scenario_ – run client and server (in case of `DEV` environment) manually with `python` to preserve 
      possibility of debugging with your IDE.
      - Run client app, using `SERVER_ENV=ENV python launcher.py`, where `ENV := [DEV | PREPROD]`.
      - Add additional environment variables if needed depends on server environment 
        (S3 secrets for `DEV`, root CA path for `PREPROD`).
    -  _Test scenario_ – run `test_execution.py`, specifying `SERVER_ENV` environment variable. This test scripts will
      run client and server (in case of `DEV` environment) for you. Client will be called as in real use-cases, with
      `datasphere` CLI command. Test script checks expected results – output files, etc. You will still have to 
      provide environment variables and program arguments, needed for client and server to run 
      (see test sources for info).
        - If you create pytest runner configuration in PyCharm for E2E tests, do the following:
          - Add `PYTHONUNBUFFERED=1` to environment variables and `-s` to additional pytest arguments so pytest will not 
          buffer client and server mock std logs.
          - In case of `SERVER_ENV=DEV`, pass server mock arguments with environment variables instead of program 
          arguments.
- Publish new version of pip package
  - Follow steps from `Setup`.
  - Update version in `version.py`, commit this change.
  - Run `tox` for tests and other checks on supported Python versions.
  - Install build tools: `pip install build twine`.
  - Run `python -m build && python -m twine upload dist/*`. PyPI auth options: 
    - https://pypi.org/help/#apitoken (for laptop publish)
    - https://pypi.org/help/#trusted-publishers (for CI publish)
- Publish examples on [GitHub](https://github.com/yandex-cloud-examples/yc-datasphere-jobs-examples).
  - Some E2E scenarios (with `description.md` public example description files) are also examples for users. 
  - To publish new examples, or sync modified ones, do the following:
    - Checkout [repo](https://github.com/yandex-cloud-examples/yc-datasphere-jobs-examples).
    - Run sync script
    ```bash
    cd tests_e2e/scenarios
    python sync_to_github.py /path/to/local/github/repo
    ```
    - Commit and push changes to repo.
- Useful links
  - https://protobuf.dev/reference/python/python-generated/
  - https://grpc.io/docs/languages/python/quickstart/
  - https://cloud.yandex.ru/docs/storage/concepts/pre-signed-urls
  - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
