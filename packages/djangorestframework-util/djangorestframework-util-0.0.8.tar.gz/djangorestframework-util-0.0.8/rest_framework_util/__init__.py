#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.8'
__history__ = """"""
__all__ = ['logger', 'INSTALLED_APPS']

import logging

logger = logging.getLogger('django.rest_framework_util')

INSTALLED_APPS = [
    'drf_spectacular',
    'drf_standardized_errors'
]
