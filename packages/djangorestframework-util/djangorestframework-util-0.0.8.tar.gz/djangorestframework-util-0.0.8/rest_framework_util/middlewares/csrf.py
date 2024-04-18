#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/21
# Tool:PyCharm

""" 主要是禁用csrf检测 """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['CsrfMiddleware']

from django.utils.deprecation import MiddlewareMixin


class CsrfMiddleware(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
