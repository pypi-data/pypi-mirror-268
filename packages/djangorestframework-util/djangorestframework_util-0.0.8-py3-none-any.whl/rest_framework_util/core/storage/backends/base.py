#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['BaseClient', 'get_file_info', 'InvalidStorageBackendError']


import io
import os
from abc import ABC, abstractmethod
from typing import NamedTuple

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _


class InvalidStorageBackendError(ImproperlyConfigured):
    pass


class FileInfo(NamedTuple):
    data: bytes
    length: int


def get_file_info(src_file):
    """ 获取文件信息

    :param str|bytes src_file: 文件
    :return: 文件信息
    :rtype: FileInfo
    """
    if isinstance(src_file, str):
        with open(src_file, 'rb') as fd:
            data = fd.read()
        length = len(data)
        data = io.BytesIO(data)
    elif isinstance(src_file, bytes):
        data = io.BytesIO(src_file)
        length = data.seek(0, os.SEEK_END)
        data.seek(0)
    else:
        raise ValueError(_('不支持文件类型'))
    return FileInfo(data=data, length=length)


class BaseClient(ABC):
    schema = 'None'

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def upload_file(self, src_file, dst_path, **kwargs):
        """ 上传文件

        :param str|bytes src_file: 文件路径(str)或文件内容(bytes)
        :param str dst_path: 目标路径
        """
        pass

    @abstractmethod
    def upload_dir(self, src_path, dst_path, **kwargs):
        """ 上传目录（即将src_path目录上传为dst_path目录）

        :param str src_path: 源路径
        :param str dst_path: 目标路径
        """
        pass

    @abstractmethod
    def download_file(self, src_path, dst_path, **kwargs):
        """ 上传文件

        :param str src_path: 文件路径
        :param str dst_path: 目标存储路径
        """
        pass

    @abstractmethod
    def download_dir(self, src_path, dst_path, **kwargs):
        """ 下载目录（即将src_path目录下载为dst_path目录）

        :param str src_path: 源路径
        :param str dst_path: 目标路径
        """
        pass

    @abstractmethod
    def delete_file(self, src_path, **kwargs):
        pass

    @abstractmethod
    def delete_dir(self, src_path, **kwargs):
        pass

    @abstractmethod
    def retrieve_file(self, src_path, **kwargs):
        pass

    @abstractmethod
    def retrieve_dir(self, src_path, **kwargs):
        pass

    @abstractmethod
    def to_http(self, path, request=None, is_original=True):
        pass

    @abstractmethod
    def close(self):
        pass
