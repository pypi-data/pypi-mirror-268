#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2024/3/6

__all__ = ['BaseService']


class BaseService:
    """ 用户角色服务 """

    def __init__(self, instance, *args, **kwargs):
        self._instance = instance

    @property
    def instance(self):
        return self._instance

    @property
    def id(self):
        return self.instance.id
