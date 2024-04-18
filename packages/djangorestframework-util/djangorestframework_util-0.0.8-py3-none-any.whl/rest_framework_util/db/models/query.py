#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['DeleteQuerySet']

from django.db.models import QuerySet
from django.utils import timezone


class DeleteQuerySet(QuerySet):
    def delete(self, delete_user_id):
        """ 逻辑删除 """
        return super(DeleteQuerySet, self).update(
            delete_user_id=delete_user_id, delete_datetime=timezone.now())

    def raw_delete(self):
        """ 物理删除 """
        return super(DeleteQuerySet, self).delete()
