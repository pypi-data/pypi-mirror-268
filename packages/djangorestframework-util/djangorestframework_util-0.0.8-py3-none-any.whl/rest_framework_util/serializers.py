#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = [
    'RelatedUserModelSerializer',
    'BaseSwitchModelSerializer',
    'BaseModelSerializer',
    'BaseRelModelSerializer',
    'BaseRelatedModelSerializer',
    'BaseSelectionModelSerializer']

import datetime

from django.contrib.auth import get_user_model
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from rest_framework_util.fields import ImageOrCharField


class BaseRelatedModelSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name')
        read_only_fields = fields


class RelatedUserModelSerializer(BaseRelatedModelSerializer):
    avatar = ImageOrCharField(
        help_text='图像,文件或地址',
        read_only=True)

    class Meta:
        model = get_user_model()
        fields = BaseRelatedModelSerializer.Meta.fields + \
            ('avatar', )


class BaseModelSerializer(BaseRelatedModelSerializer):
    create_user = RelatedUserModelSerializer(read_only=True, help_text='创建用户')
    update_user = RelatedUserModelSerializer(read_only=True, help_text='更新用户')
    description = serializers.CharField(
        required=False, allow_blank=True, allow_null=True, help_text='描述')
    create_ts = serializers.SerializerMethodField()
    update_ts = serializers.SerializerMethodField()

    class Meta:
        fields = BaseRelatedModelSerializer.Meta.fields + (
            # 'description',
            'create_user',
            'update_user',
            'create_datetime',
            'update_datetime',
            'create_ts',
            'update_ts',
        )
        read_only_fields = fields

    @staticmethod
    def get_ts_by_field(obj, field_name):
        dt = getattr(obj, field_name, None)
        ts = None if not dt else int(dt.replace(
            tzinfo=datetime.timezone.utc).timestamp())
        return ts

    @extend_schema_field(OpenApiTypes.INT)
    def get_create_ts(self, obj):
        return self.get_ts_by_field(obj, 'create_datetime')

    @extend_schema_field(OpenApiTypes.INT)
    def get_update_ts(self, obj):
        return self.get_ts_by_field(obj, 'update_datetime')

    @extend_schema_field(OpenApiTypes.INT)
    def get_delete_ts(self, obj):
        return self.get_ts_by_field(obj, 'delete_datetime')


class BaseRelModelSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        pass


class BaseSwitchModelSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(help_text='是否激活')

    class Meta:
        fields = ('id', 'is_active')
        read_only_fields = ('id', )


class BaseSelectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description')
        read_only_fields = fields
