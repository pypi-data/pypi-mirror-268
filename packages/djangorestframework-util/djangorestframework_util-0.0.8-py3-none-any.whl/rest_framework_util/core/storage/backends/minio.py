#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['Client']

import mimetypes
import os.path


from rest_framework_util.core.storage.backends.base import BaseClient, get_file_info


class Client(BaseClient):
    schema = 'minio'

    def __init__(self, *args, **kwargs):
        import minio
        public_address = kwargs.pop('public_address', None)
        private_address = kwargs.pop('private_address', None)
        self.__minio = minio.Minio(*args, **kwargs)
        self.public_address = public_address or self.minio._base_url._url.geturl()
        self.private_address = private_address or self.minio._base_url._url.geturl()
        super().__init__(*args, **kwargs)

    @property
    def minio(self):
        return self.__minio

    @minio.setter
    def minio(self, value):
        self.__minio = value

    @staticmethod
    def split_path(path):
        """ 分割路径

        :param str path: minio路径
        :return: (bucket_name, prefix, file_name)
        :rtype: tuple
        """
        seq = '/'
        while path.startswith(seq):
            path = path[1:]
        if path.count(seq) <= 0:
            return path, None, None
        bucket_name, path = path.split('/', maxsplit=1)
        if path.count(seq) <= 0:
            return bucket_name, '', path
        prefix, file_name = path.rsplit(seq, maxsplit=1)
        return bucket_name, prefix, file_name

    @staticmethod
    def split_prefix(path):
        """ 分割路径

        :param str path: minio路径
        :return: (bucket_name, prefix)
        :rtype: tuple
        """
        seq = '/'
        while path.startswith(seq):
            path = path[1:]
        if path.count(seq) < 0:
            return path, None
        bucket_name, prefix = path.split('/', maxsplit=1)
        return bucket_name, prefix

    @staticmethod
    def get_object_name(prefix, file_name):
        """ 获取minio格式对象名称

        :param str prefix: 路径
        :param str file_name: 文件名称
        :return: 对象名称
        :rtype: str|None
        """
        if file_name is None:
            return None
        if prefix == '/':
            return f'{file_name}'
        prefix = Client.format_prefix(prefix)
        # 路径保护
        if file_name.find('/') != -1:
            file_name = file_name.replace('/', '')
        return f'{prefix}{file_name}'

    @staticmethod
    def format_prefix(prefix):
        """ 格式化路径为linux格式，同时追加/

        :param str prefix: 前缀
        :return: 路径
        :rtype: str
        """
        assert isinstance(prefix, str)
        prefix = prefix.replace('\\', '/')
        prefix = prefix.strip('/')
        if not prefix.endswith('/'):
            prefix += '/'
        return prefix

    def upload_file(self, src_file, dst_path, content_type=None, **kwargs):
        dst_path = dst_path.replace('\\', '/')
        bucket_name, prefix, file_name = self.split_path(dst_path)
        file_info = get_file_info(src_file)
        if content_type is None:
            content_type, _ = mimetypes.guess_type(file_name)
            if content_type is None:
                content_type = 'application/octet-stream'
        object_name = self.get_object_name(
            prefix=self.format_prefix(prefix), file_name=file_name)
        self.minio.put_object(
            bucket_name=bucket_name,
            object_name=object_name,
            data=file_info.data,
            length=file_info.length,
            content_type=content_type,
            **kwargs
        )

    def upload_dir(self, src_path, dst_path, **kwargs):
        dst_path = dst_path.replace('\\', '/')
        if not os.path.isdir(src_path):
            return
        for name in os.listdir(src_path):
            # if name in ('__pycache__', ):
            #     continue
            path = os.path.join(src_path, name)
            _dst_path = os.path.join(dst_path, name)
            if os.path.isdir(path):
                self.upload_dir(path, _dst_path, **kwargs)
            else:
                self.upload_file(path, _dst_path, **kwargs)

    def download_file(self, src_path, dst_path, **kwargs):
        bucket_name, prefix, file_name = self.split_path(src_path)
        object_name = self.get_object_name(prefix, file_name)
        dir_path = os.path.dirname(dst_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        self.minio.fget_object(bucket_name, object_name, dst_path)

    def download_dir(self, src_path, dst_path, **kwargs):
        bucket_name, prefix = self.split_prefix(src_path)
        prefix = self.format_prefix(prefix)
        if prefix == '/':
            return
        objects = self.minio.list_objects(
            bucket_name=bucket_name,
            prefix=prefix,
        )
        dir_name = os.path.basename(prefix)
        import posixpath
        if not os.path.isdir(dst_path):
            os.makedirs(dst_path, exist_ok=True)
        for obj in objects:
            if obj.is_dir:
                _src_path = bucket_name + obj.object_name
                _dst_path = os.path.join(dst_path, dir_name)
                self.download_dir(_src_path, _dst_path)
            else:
                rel_path = posixpath.relpath(
                    path=obj.object_name, start=prefix)
                local_path = os.path.join(dst_path, rel_path)
                self.minio.fget_object(
                    bucket_name, obj.object_name, local_path)

    def delete_file(self, src_path, **kwargs):
        bucket_name_name, prefix, file_name = self.split_path(src_path)
        object_name = self.get_object_name(prefix=prefix, file_name=file_name)
        self.minio.remove_object(
            bucket_name_name,
            object_name,
            **kwargs)

    def delete_dir(self, src_path, **kwargs):
        # FIXME(fengdy):删除有错误
        bucket_name, prefix = self.split_prefix(src_path)
        deleted_object_list = map(
            lambda x: x.object_name,
            self.minio.list_objects(bucket_name, prefix, recursive=True),
        )
        errors = self.minio.remove_objects(bucket_name, deleted_object_list)
        if errors:
            raise ValueError(';'.join(errors))

    def retrieve_file(self, src_path, **kwargs):
        return None

    def retrieve_dir(self, src_path, **kwargs):
        return None

    def to_http(self, path, request=None, is_original=True):
        if request is not None:
            if 'X-Inner-Ip' in list(request.headers.keys()):
                is_original = True
            else:
                is_original = False
        if is_original:
            result = self.private_address + path
        else:
            result = self.public_address + path
        return result

    def close(self):
        self.minio = None
