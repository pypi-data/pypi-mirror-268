import logging
import os
from pathlib import Path
import tempfile
from typing import Dict, List, Union, BinaryIO
from zipfile import ZipFile

import requests

from datasphere.config import VariablePath, local_module_prefix
from datasphere.utils import humanize_bytes_size
from datasphere.pyenv import PythonEnv

from datasphere.api import jobs_pb2 as jobs

logger = logging.getLogger(__name__)


def prepare_local_modules(py_env: PythonEnv, tmpdir: str) -> List[VariablePath]:
    result = []
    for i, module in enumerate(py_env.local_modules_paths):
        logger.debug('zip local module `%s` ...', module)
        with tempfile.NamedTemporaryFile('rb', dir=tmpdir, delete=False) as ar:
            zip_path(module, ar)

            # Path does not matter for local module since it will be unzipped to correct location, also, lzy
            # determines local module path as absolute path in general case, so we give it utility var value.
            path = VariablePath(ar.name, var=f'{local_module_prefix}_{i}')
            path.get_file(ar)

            result.append(path)

    return result


def zip_path(path: Union[str, Path], zip_fileobj: BinaryIO) -> None:
    with ZipFile(zip_fileobj.name, 'w') as z:
        _zip_path(path, z)

    zip_fileobj.seek(0)


def _zip_path(path: Union[str, Path], zip_file: ZipFile) -> None:
    path = Path(path)
    relative_to = path.parent

    paths: List[Path] = []
    if path.is_dir():
        for root, _, files in os.walk(path):
            paths.extend(Path(root) / filename for filename in files)
    else:
        paths.append(path)

    for path_at_fs in paths:
        path_to_write = path_at_fs.relative_to(relative_to)
        zip_file.write(path_at_fs, path_to_write)


def _get_total_size(files: List[jobs.StorageFile]) -> str:
    return humanize_bytes_size(sum(f.file.size_bytes for f in files))


def upload_files(files: List[jobs.StorageFile], sha256_to_display_path: Dict[str, str]):
    # Maybe add debug log about already uploaded files.
    if len(files) == 0:
        logger.info('no files to upload')
        return
    logger.info('uploading %d files (%s) ...', len(files), _get_total_size(files))
    for f in files:
        with open(f.file.desc.path, 'rb') as fd:
            display_path = sha256_to_display_path.get(f.file.sha256, f.file.desc.path)
            logger.debug('uploading file `%s` (%s) ...', display_path, humanize_bytes_size(f.file.size_bytes))
            if not f.url:
                continue
            resp = requests.put(f.url, data=fd)
            resp.raise_for_status()
    logger.info('files are uploaded')


def download_files(files: List[jobs.StorageFile]):
    if len(files) == 0:
        logger.info('no files to download')
        return
    logger.info('downloading %d files (%s) ...', len(files), _get_total_size(files))
    for f in files:
        logger.debug('downloading file `%s` (%s) ...', f.file.desc.path, humanize_bytes_size(f.file.size_bytes))
        resp = requests.get(f.url)
        resp.raise_for_status()
        path = Path(f.file.desc.path)
        if not path.parent.exists():
            # Create dirs containing output file.
            path.parent.mkdir(parents=True)
        with path.open('wb') as fd:
            for chunk in resp.iter_content(chunk_size=1 << 24):  # 16Mb chunk
                fd.write(chunk)
    logger.info('files are downloaded')
