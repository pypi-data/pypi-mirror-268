#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/21
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['AgentMiddleware']

from django.contrib.auth.middleware import get_user
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject


class AgentMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.user = SimpleLazyObject(lambda: get_user(request))
        request.is_doc_request = lambda: bool(
            'doc/schema/' in request.path
        )
        request.is_login_exempt = lambda: bool(False)
