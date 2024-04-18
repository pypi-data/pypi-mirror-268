#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['RelatedUserField', 'ImageOrCharField']

import os
from copy import deepcopy

from django.contrib.auth import get_user_model
from rest_framework import serializers

from rest_framework_util import logger
from rest_framework_util.core.storage import storage
from shortcut_util.unique import uuid_id


class ImageOrCharField(serializers.CharField):
    """ 字符串类型的图像，上传的是url
    """

    def __init__(self, **kwargs):
        _image_kwargs = {
            'allow_empty_file': kwargs.pop('allow_empty_file', False),
        }
        if 'use_url' in kwargs:
            _image_kwargs['use_url'] = kwargs.pop('use_url')
        _char_kwargs = {
            'allow_blank': kwargs.pop('allow_blank', False),
            'trim_whitespace': kwargs.pop('trim_whitespace', True),
            'min_length': kwargs.pop('min_length', None)
        }
        self.storage = kwargs.pop('storage', storage)
        _image_kwargs.update(deepcopy(kwargs))
        self.image_field = serializers.ImageField(**_image_kwargs)
        _char_kwargs.update(kwargs)
        super(ImageOrCharField, self).__init__(**_char_kwargs)

    def save_image(self, image_obj):
        ext_name = os.path.splitext(image_obj.name)[1] or '.png'
        file_name = f'{uuid_id()}{ext_name}'
        file_path = os.path.join(self.dir_path, file_name)
        path = self.storage.upload_file(
            image_obj.read(), file_path)
        return path

    def to_internal_value(self, data):
        try:
            # `UploadedFile` objects should have name and size attributes.
            data.name and data.size
        except AttributeError:
            return super(ImageOrCharField, self).to_internal_value(data)
        image_obj = self.image_field.to_internal_value(data)
        return self.save_image(image_obj)

    def to_representation(self, value):
        if not value:
            return None
        value = super(ImageOrCharField, self).to_representation(value)
        if value.startswith('http'):
            return value
        url = self.storage.to_http(value, request=self.context['request'])
        return url


class RelatedUserField(serializers.CharField):
    def __init__(self, **kwargs):
        kwargs['read_only'] = True
        self.serializer_class = kwargs.get(
            'serializer_class', None)
        if self.serializer_class is None:
            from rest_framework_util.serializers import RelatedUserModelSerializer
            self.serializer_class = RelatedUserModelSerializer
        super().__init__(**kwargs)

    def to_representation(self, value):
        if not value:
            return None
        try:
            user = get_user_model().objects.get(pk=value)
        except BaseException:
            logger.exception(f'can not get user by pk. pk={value}')
            return None
        return self.serializer_class(
            instance=user, context=self.parent.context).data
