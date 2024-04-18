# -*- coding: utf-8 -*-
"""
Copyright(C) 2023 baidu, Inc. All Rights Reserved

# @Time : 2023/9/5 17:14
# @Author : yangtingyu01
# @Email: yangtingyu01@baidu.com
# @File : __init__.py.py
# @Software: PyCharm
"""
from typing import Dict, Optional
import os

from .s3 import S3BlobStore
from .blobstore import KIND_S3, CONFIG_HOST, blobstore_config


def blobstore(filesystem=None, kind: str = None,  endpoint: str = None, config: Optional[Dict] = None):
    """
    Initialize a blobstore.

    Args:
        kind: blobstore kind
        filesystem: filesystem
        endpoint: blobstore endpoint
        config: blobstore config
    """
    if filesystem is not None:
        kind, endpoint, config = blobstore_config(filesystem=filesystem)

    if kind == KIND_S3:
        return S3BlobStore(endpoint=endpoint, config=config)
    else:
        raise ValueError("Unsupported filesystem kind: {}".format(kind))


def download_by_filesystem(filesystem, file_path: str, dest_path: str):
    """
    Download a file by filesystem.
    """
    client = blobstore(filesystem=filesystem)

    meta_list = client.list_meta(path=file_path)
    for meta in meta_list:
        dest_file = os.path.join(dest_path, meta.name)
        if not os.path.exists(os.path.dirname(dest_file)):
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
        client.download_file(path=meta.url_path, file_name=dest_file)


def upload_by_filesystem(filesystem, file_path: str, dest_path: str):
    """
    Upload a file by filesystem.
    """
    client = blobstore(filesystem=filesystem)

    if os.path.isfile(file_path):
        client.upload_file(file_name=file_path, path=dest_path)

    if os.path.isdir(file_path):
        for root, _, files in os.walk(file_path):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, file_path)
                remote_path = os.path.join(dest_path, relative_path)
                client.upload_file(file_name=local_path, path=remote_path)


def init_py_filesystem(filesystem):
    """
    Initialize a py filesystem.
    Args:
        filesystem: filesystem
    """
    import s3fs
    from pyarrow.fs import PyFileSystem, FSSpecHandler

    s3_fs = s3fs.S3FileSystem(
        key=filesystem["credential"]["accessKey"],
        secret=filesystem["credential"]["secretKey"],
        client_kwargs={
            'endpoint_url': filesystem[CONFIG_HOST]
        }
    )

    return PyFileSystem(FSSpecHandler(s3_fs))
