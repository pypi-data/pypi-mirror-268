#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/21
# Tool:PyCharm

""" 日志记录 """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['LogMiddleware']

import json

from django.core.files import File
from django.utils.translation import gettext_lazy as _
from django.utils.deprecation import MiddlewareMixin

from rest_framework_util import logger


class LogMiddleware(MiddlewareMixin):

    @staticmethod
    def get_request_data_log(request):
        data = {}
        if 'application/json' in request.content_type:
            if request.body:
                try:
                    data = json.loads(request.body.decode())
                except BaseException:
                    logger.exception(_('解析请求数据异常'))
                    pass
        # TODO(fengdy): 有的时候获取不到数据，使用put方法，multipart/form-data
        for key, value in list(request.POST.items()) + \
                list(request.FILES.items()):
            try:
                if isinstance(value, File):
                    value = f'File(content_type={value.content_type}, name={value.name}, size={value.size})'
                data[key] = value
            except BaseException:
                logger.exception(_('获取body数据异常'))
                pass
        return data

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            view_name = view_func.cls.__name__
        except BaseException:
            view_name = view_func
        message_dict = {
            'request_id': request.META.get('HTTP-X-Request-Id', None),
            'user_id': request.user.id,
            'method': request.method,
            'url': request.get_full_path(),
            'data': self.get_request_data_log(request),
            'args': view_args,
            'kwargs': view_kwargs
        }
        message = json.dumps(message_dict, indent=2)
        logger.info(f'{view_name}(\n{message})')
