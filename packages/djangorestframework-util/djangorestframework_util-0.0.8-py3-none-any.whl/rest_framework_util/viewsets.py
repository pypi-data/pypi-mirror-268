#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/12/14
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = [
    'BaseRelModelViewSet',
    'BaseModeViewSet',
    'BaseFileUploadAPIView',
    'RetrieveSerializerViewSet']

from abc import ABC, abstractmethod

from django.db.models import Q
from django.utils import timezone
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from rest_framework_util.core.upload.settings import UploadSettings
from rest_framework_util.core.upload.backends import upload, merge
from rest_framework_util.exceptions import HTTP404
from rest_framework_util.mixins import CreateRelModelMixin, DestroyRelModelMixin, UpdateRelModelMixin


class RetrieveSerializerViewSet:
    def get_serializer_class(self):
        """ 根据固定格式获取 """
        serializer_class = super().get_serializer_class()
        action_name = ''
        for _action in self.action.split('_'):
            action_name += _action.capitalize()
        serializer_class_name = action_name + serializer_class.__name__
        serializer_class = getattr(
            self.serializer_module,
            serializer_class_name,
            serializer_class)
        return serializer_class


class GenericRelViewSet(RetrieveSerializerViewSet, GenericViewSet):
    parent_key = None
    parent_model = None

    def get_parent_key(self):
        return self.parent_key or f'{self.parent_model.__name__.lower()}_id'

    def get_parent_object(self):
        key = '_parent_object_'
        if hasattr(self, key):
            instance = getattr(self, key)
        else:
            try:
                instance = self.parent_model.objects.get(
                    pk=self.kwargs[self.get_parent_key()])
            except self.parent_model.DoesNotExist:
                raise HTTP404()
            setattr(self, key, instance)
        return instance

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['parent'] = self.get_parent_object()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        key = self.get_parent_key()
        kwargs = {
            key: self.kwargs[key]
        }
        return queryset.filter(**kwargs)


class BaseRelModelViewSet(mixins.ListModelMixin,
                          CreateRelModelMixin,
                          UpdateRelModelMixin,
                          DestroyRelModelMixin,
                          GenericRelViewSet):
    pass


class BaseModeViewSet(RetrieveSerializerViewSet, ModelViewSet):
    http_method_names = [
        "get",
        "post",
        # "put",
        "patch",
        "delete",
        "head",
        "options",
        "trace",
    ]
    serializer_module = None

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'selection':
            # 过滤未激活以及过期的
            queryset = queryset.filter(is_active=True)
            model = self.serializer_class.Meta.model
            if hasattr(model, 'expire_datetime'):
                queryset = queryset.filter(Q(expire_datetime__isnull=True) | Q(
                    expire_datetime__lt=timezone.now()))
        return queryset

    def perform_create(self, serializer, **kwargs):
        serializer.save(create_user_id=self.request.user.id, **kwargs)

    def perform_update(self, serializer, **kwargs):
        serializer.save(update_user_id=self.request.user.id, **kwargs)

    @action(detail=True, methods=['PATCH'])
    def switch(self, request, *args, **kwargs):
        """ 启用/禁用 """
        return self.update(request, *args, **kwargs)

    @action(detail=False, methods=['GET'], url_path='selection')
    def select(self, request, *args, **kwargs):
        """ 下拉选择 """
        return self.list(request, *args, **kwargs)


class BaseFileUploadAPIView(APIView, ABC):
    app_settings = None

    def get_app_settings(self):
        assert self.app_settings is not None, (
            "'%s' should either include a `app_settings` attribute, "
            "or override the `get_app_settings()` method."
            % self.__class__.__name__
        )
        assert isinstance(self.app_settings, UploadSettings), (
            "'%s' is not subclass of UploadSettings"
            % self.__class__.__name__
        )
        return self.app_settings

    @abstractmethod
    def get_file_view(self, request):
        pass

    def post(self, request, *args, **kwargs):
        return upload(request,
                      self.get_file_view(request),
                      request.data['file'],
                      self.get_app_settings())


class BaseFileMergeAPIView(BaseFileUploadAPIView, ABC):
    def post(self, request, *args, **kwargs):
        return merge(request,
                     self.get_file_view(request),
                     self.get_app_settings())
