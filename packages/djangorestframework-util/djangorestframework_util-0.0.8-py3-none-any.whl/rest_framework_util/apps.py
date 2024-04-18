#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/12/7
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['AppProxy']

from django.conf import settings


class AppProxy:
    @staticmethod
    def has_role(self):
        return 'role' in settings.INSTALLED_APPS

    @staticmethod
    def has_permission(self):
        return 'permission' in settings.INSTALLED_APPS
