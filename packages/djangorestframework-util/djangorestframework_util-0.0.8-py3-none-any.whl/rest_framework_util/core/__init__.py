#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['get_storage']

from django.conf import settings
from rest_framework.settings import import_from_string


def get_storage(api_settings=None):
    api_settings = api_settings or settings
    storage_setting = api_settings.STORAGE
    _class = import_from_string(storage_setting['ENGINE'], 'ENGINE')
    instance = _class(storage_setting['OPTIONS'])
    return instance
