#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/21
# Tool:PyCharm

""" 追踪，增加请求id、时间等 """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['TraceMiddleware']

import time

from django.utils.deprecation import MiddlewareMixin

from shortcut_util.unique import uuid_id


class TraceMiddleware(MiddlewareMixin):
    request_ts_key = '_request_ts'

    def process_request(self, request):
        request.META['HTTP-X-Request-Id'] = request.META.get(
            'HTTP-X-Request-Id', uuid_id())
        setattr(request, self.request_ts_key, int(time.time() * 1000))

    def process_response(self, request, response):
        response.headers['HTTP-X-Request-Id'] = request.META['HTTP-X-Request-Id']
        request_ts = getattr(request, self.request_ts_key)
        response_ts = int(time.time() * 1000)
        response.headers['HTTP-X-Use-Time'] = int(response_ts - request_ts)
        return response
