#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/4/12
# Tool:PyCharm

""" Json响应统一处理 """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['ResponseMiddleware']

from django.conf import settings
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from rest_framework_util.exceptions import HTTP500
from rest_framework_util.response import ResponseData


class ResponseMiddleware(MiddlewareMixin):
    """ 统一异常响应数据，前台只支持以下状态码

    * 200、401、422、403、404、500、502、504

    """
    supported_stats_codes = (200, 401, 422, 403, 404, 500, 502, 504)

    def process_response(self, request, response):
        if request.is_doc_request():
            return response
        status_code = response.status_code
        if status_code in (301, 302):
            return response
        if not any([status.is_server_error(status_code),
                   status.is_client_error(status_code)]):
            if isinstance(response, TemplateResponse):
                pass
            else:
                response.status_code = 200
                if hasattr(response, 'data'):
                    response.data = ResponseData(data=response.data).todict()
                    response.content = JSONRenderer().render(response.data)
        else:
            if status_code == status.HTTP_404_NOT_FOUND:
                pass
            if status_code == 401:
                if request.path.endswith('/o/authorize/') or request.path.endswith('/o/token/'):
                    redirect_uri = request.GET.get('redirect_uri', None)
                    if request.GET.get('redirect_uri'):
                        query_param = f'/#/login?redirect_uri={redirect_uri}'
                    else:
                        query_param = ''
                    return HttpResponseRedirect(settings.INDEX_URL+query_param)
            # if status_code == 400:
            #     if request.path.endswith('/o/authorize/') or request.path.endswith('/o/token/'):
            #         return response
            if 'application/json' not in response.headers['Content-Type']:
                if request.path.startswith('/auth/oauth/'):
                    return response
                response.headers['Content-Type'] = 'application/json'
                response.data = HTTP500().response_data()
                response.content = JSONRenderer().render(response.data)
            if status_code not in self.supported_stats_codes:
                response.status_code = 500
            # logger.warning(f'API response. status_code={status_code}.')
        return response
