import hashlib
import os
import pathlib
import shutil
import tarfile
import tempfile
from typing import Any, Optional, Union


def calculate_md5(fpath: Union[str, pathlib.Path], chunk_size: int = 1024 * 1024) -> str:
    md5 = hashlib.md5()
    with open(fpath, "rb") as f:
        while chunk := f.read(chunk_size):
            md5.update(chunk)
    return md5.hexdigest()


def check_md5(fpath: Union[str, pathlib.Path], md5: str, **kwargs: Any) -> bool:
    return md5 == calculate_md5(fpath, **kwargs)


def extract_tar(from_path: Union[str, pathlib.Path], to_path: Union[str, pathlib.Path]) -> None:
    with tarfile.open(from_path, "r") as tar:
        tar.extractall(to_path)


def extract_archive(from_path: Union[str, pathlib.Path], to_path: Optional[Union[str, pathlib.Path]] = None, remove_finished: bool = False) -> Union[str, pathlib.Path]:
    if to_path is None:
        to_path = pathlib.Path(from_path).parent

    extract_tar(from_path, to_path)
    if remove_finished:
        os.remove(from_path)

    return to_path


def copy_and_extract_tars(from_dir: Union[str, pathlib.Path], to_dir: Optional[Union[str, pathlib.Path]] = None) -> list[Union[str, pathlib.Path]]:
    if to_dir is None:
        to_dir = tempfile.mkdtemp()

    tar_files = []
    for src in pathlib.Path(from_dir).glob("*.tar"):
        if tarfile.is_tarfile(src):
            dst = to_dir / src.name
            tar_files.append(dst)

            if dst.is_file():
                md5 = calculate_md5(src)
                if check_md5(dst, md5):
                    continue

            shutil.copy(src, dst)

    for from_path in tar_files:
        extract_tar(from_path, to_dir)

    return tar_files
