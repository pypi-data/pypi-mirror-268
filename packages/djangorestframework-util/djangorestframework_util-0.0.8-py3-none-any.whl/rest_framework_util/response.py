#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/4/12
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['ResponseData']

from typing import NamedTuple


class _ResponseDataTuple(NamedTuple):
    code: int
    message: str
    data: object
    detail: object


class ResponseData:
    def __init__(self, code=200, message='', data=None, detail=None):
        self.__data = _ResponseDataTuple(code, message, data, detail)

    def todict(self):
        data = self.__data._asdict()
        data.pop('detail', None)
        return data

    def __getattr__(self, item):
        return getattr(self.__data, item)
