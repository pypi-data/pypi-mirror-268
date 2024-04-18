#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/2/27
# Tool:PyCharm

"""  """
from __future__ import unicode_literals

__version__ = '0.0.1'
__history__ = """"""

import logging

from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from drf_standardized_errors.formatter import ExceptionFormatter as _ExceptionFormatter
from drf_standardized_errors.types import ErrorResponse, ErrorType

from rest_framework_util.response import ResponseData


class BaseException(Exception):
    ERROR_CODE = "0000000"
    MESSAGE = _("APP Error")
    STATUS_CODE = 500
    LOG_LEVEL = logging.ERROR

    def __init__(self, message: str = None,
                 data: object = None, *args, **kwargs):
        super(BaseException, self).__init__(*args)
        self.message = self.MESSAGE if message is None else message
        self.data = data

    def render_data(self):
        return self.data

    def response_data(self):
        return ResponseData(code=self.ERROR_CODE,
                            message=self.message,
                            data=self.render_data()).todict()

    def to_response(self):
        response = JsonResponse(self.response_data())
        response.status_code = self.STATUS_CODE
        return response


class HTTP400(BaseException):
    MESSAGE = _("ClientError")
    ERROR_CODE = "40000"
    STATUS_CODE = 400


class ParamValidationError(HTTP400):
    MESSAGE = _("ParamValidationError")
    ERROR_CODE = "40001"


class HTTP401(BaseException):
    MESSAGE = _("AccessForbidden")
    ERROR_CODE = "40100"
    STATUS_CODE = 401


class HTTP403(BaseException):
    MESSAGE = _("AccessForbidden")
    ERROR_CODE = "40300"
    STATUS_CODE = 403


class HTTP404(BaseException):
    MESSAGE = _("NotFound")
    ERROR_CODE = "40400"
    STATUS_CODE = 404


class HTTP405(BaseException):
    MESSAGE = _("MethodError")
    ERROR_CODE = "40500"
    STATUS_CODE = 405


class HTTP500(BaseException):
    MESSAGE = _("ServerError")
    ERROR_CODE = "50000"
    STATUS_CODE = 500


class ExceptionFormatter(_ExceptionFormatter):
    def format_error_response(self, error_response: ErrorResponse):
        messages = []
        codes = []
        for error in error_response.errors:
            if not error.attr or error.attr in ('non_field_errors', ):
                messages.append(f'{error.detail}')
            else:
                messages.append(f'{error.attr}:{error.detail}')
            codes.append(error.code)

        message = ';'.join(messages)
        if error_response.type == ErrorType.VALIDATION_ERROR:
            exception_class = ParamValidationError
        elif error_response.type == ErrorType.CLIENT_ERROR:
            if 'permission_denied' in codes or 'method_not_allowed' in codes:
                exception_class = HTTP403
            else:
                exception_class = HTTP400
        else:
            exception_class = HTTP500
        return exception_class(message=message).response_data()
