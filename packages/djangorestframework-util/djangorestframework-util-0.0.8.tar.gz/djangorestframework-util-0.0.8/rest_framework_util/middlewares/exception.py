#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/2/27
# Tool:PyCharm

""" APP服务异常通用处理 """
__version__ = '0.0.1'
__history__ = """"""


import json
import traceback

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from rest_framework_util import logger
from rest_framework_util.exceptions import BaseException, HTTP500


class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        # 用户自我感知的异常抛出
        if isinstance(exception, BaseException):
            logger.log(
                exception.LOG_LEVEL,
                (
                    """Throw Exception->[%s] status_code->[%s] & """
                    """client_message->[%s] & args->[%s] """
                )
                % (
                    traceback.format_exc(),
                    exception.ERROR_CODE,
                    exception.message,
                    exception.args,
                ),
            )

            response = JsonResponse(exception.response_data())
            response.status_code = exception.STATUS_CODE
            return response

        # 用户未主动捕获的异常
        logger.error(
            """Raise Exception->[%s], URL->[%s]"""
            """Method->[%s]"""
            """Params->[%s]"""
            % (
                traceback.format_exc(),
                request.path,
                request.method,
                json.dumps(getattr(request, request.method, None)),
            )
        )

        # 对于check开头函数进行遍历调用，如有满足条件的函数，则不屏蔽异常
        check_functions = self.get_check_functions()
        for check_function in check_functions:
            if check_function():
                return None

        return HTTP500().to_response()

    def get_check_functions(self):
        """获取需要判断的函数列表"""
        return [
            getattr(self, func)
            for func in dir(self)
            if func.startswith("check") and callable(getattr(self, func))
        ]
