#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['Client']

import os
import shutil

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from rest_framework_util.core.storage.backends.base import BaseClient, get_file_info

DEFAULT_ROOT_PATH = settings.BASE_DIR / 'storage'


class Client(BaseClient):

    schema = 'local'

    def __init__(self, root_path=None):
        self.root_path = root_path or DEFAULT_ROOT_PATH

    def get_abs_path(self, path):
        while path.startswith('/'):
            path = path[1:]
        path = os.path.join(self.root_path, path)
        return path

    def upload_file(self, src_file, dst_path):
        while dst_path.startswith('/'):
            dst_path = dst_path[1:]
        dst_path = os.path.join(self.root_path, dst_path)
        dir_path = os.path.dirname(dst_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        file_info = get_file_info(src_file)
        with open(dst_path, 'wb') as fd:
            fd.write(file_info.data.read())

    def upload_dir(self, src_path, dst_path, **kwargs):
        abs_dst_path = self.get_abs_path(dst_path)
        shutil.copytree(src_path, abs_dst_path)

    def download_file(self, src_path, dst_path, **kwargs):
        abs_src_path = self.get_abs_path(src_path)
        if not os.path.isfile(abs_src_path):
            raise ValueError(_(f'文件[{src_path}]不存在'))
        dir_path = os.path.dirname(dst_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        shutil.copyfile(src_path, dst_path)

    def download_dir(self, src_path, dst_path, **kwargs):
        abs_src_path = self.get_abs_path(src_path)
        shutil.copytree(abs_src_path, dst_path)

    def delete_file(self, src_path, **kwargs):
        abs_src_path = self.get_abs_path(src_path)
        if os.path.isfile(abs_src_path):
            os.remove(abs_src_path)

    def delete_dir(self, src_path, **kwargs):
        abs_src_path = self.get_abs_path(src_path)
        if os.path.isdir(abs_src_path):
            shutil.rmtree(abs_src_path)

    def retrieve_file(self, src_path, **kwargs):
        return None

    def retrieve_dir(self, src_path, **kwargs):
        return None

    def to_http(self, path, request=None, is_original=True):
        return path

    def close(self):
        pass
