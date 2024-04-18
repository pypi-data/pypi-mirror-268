#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/3/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['PageNumberPagination']
from collections import OrderedDict
from math import ceil

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination as _PageNumberPagination
from rest_framework.response import Response

from rest_framework_util import exceptions


class PageNumberPagination(_PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def __init__(self):
        self.__queryset = None
        self.__page_not_found = False
        self.__page_size = None

    def paginate_queryset(self, queryset, request, view=None):
        # TODO(fengdy): page_number为空或0时表示不分页
        page_size = self.get_page_size(request)
        self.__page_size = page_size
        try:
            page_number = int(
                request.query_params.get(
                    self.page_query_param, 0) or 1)
        except Exception:
            raise exceptions.ParamValidationError(message=_('页码需要为整数'))
        if not page_size or int(page_number) == -1:
            self.__queryset = queryset
            return queryset
        try:
            return super().paginate_queryset(queryset, request, view)
        except NotFound:
            self.__page_not_found = True
            self.__queryset = queryset
            return list(queryset.none())
        except Exception as exc:
            raise exc

    def get_paginated_response(self, data):
        """ 重定义输出的数据结构 """
        if self.__queryset is not None and not self.__page_not_found:
            # 不分页
            total = self.__queryset.count()
            page_total = 1
            results = data
        else:
            if self.__page_not_found:
                # 分页但页码超限
                total = self.__queryset.count()
                page_total = ceil(total / self.__page_size)
                results = []
            else:
                # 正常分页
                total = self.page.paginator.count
                page_total = self.page.paginator.num_pages
                results = data
        response = Response(OrderedDict([
            ('total', total),
            ('page_total', page_total),
            ('data', results)
        ]))
        return response
