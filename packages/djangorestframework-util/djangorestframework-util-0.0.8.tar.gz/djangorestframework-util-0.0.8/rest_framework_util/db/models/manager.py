#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['UserModelManager', 'BaseModelManager']

from django.contrib.auth.models import UserManager
from django.db.models.manager import BaseManager

from rest_framework_util.db.models.query import DeleteQuerySet


class BaseModelManager(BaseManager.from_queryset(DeleteQuerySet)):
    def get_queryset(self):
        return super().get_queryset().filter(delete_datetime__isnull=True)


class UserModelManager(BaseModelManager, UserManager):
    pass
