#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['BaseModel', 'BaseRelModel']

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework_util import exceptions, logger
from rest_framework_util.db.models.manager import BaseModelManager
from shortcut_util.unique import uuid_id

User = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default=uuid_id)
    is_active = models.BooleanField('是否激活', default=True)
    create_user = models.ForeignKey(
        User,
        models.RESTRICT,
        related_name="created_%(app_label)s_%(class)ss"
    )
    create_datetime = models.DateTimeField('创建时间', auto_now_add=True)
    update_user = models.ForeignKey(
        User,
        models.SET_NULL,
        related_name="updated_%(app_label)s_%(class)ss",
        blank=True, null=True)
    update_datetime = models.DateTimeField(
        '更新时间', blank=True, null=True, auto_now=True)
    name = models.CharField('名称', max_length=64)
    description = models.CharField('描述', max_length=256, blank=True)

    delete_user = models.ForeignKey(
        User,
        models.SET_NULL,
        related_name="deleted_%(app_label)s_%(class)ss",
        blank=True, null=True)
    delete_datetime = models.DateTimeField('删除时间', blank=True, null=True)
    objects = BaseModelManager()

    class Meta:
        abstract = True

    def delete(self, delete_user_id, using=None, keep_parents=False):
        from django.db import router, IntegrityError
        from django.db.models.deletion import Collector
        using = using or router.db_for_write(self.__class__, instance=self)
        assert self.pk is not None, (
            "%s object can't be deleted because its %s attribute is set to None." %
            (self._meta.object_name, self._meta.pk.attname)
        )

        collector = Collector(using=using)
        try:
            collector.collect([self], keep_parents=keep_parents)
        except IntegrityError:
            raise exceptions.HTTP403(message=_('存在关联对象，不允许删除'))
        self.delete_user_id = delete_user_id
        self.delete_datetime = timezone.now()
        self.save()
        logger.info(f'delete {self}. user_id={delete_user_id}')
        return 1, {self._meta.label: 1}

    @property
    def is_deleted(self):
        return self.delete_datetime is not None

    def extended_strs(self):
        return []

    def __str__(self):
        strs = [f'id={self.id}', f'name={self.name}'] + self.extended_strs()
        return f'{self.__class__.__name__}({",".join(strs)})'


class BaseRelModel(BaseModel):
    class Meta:
        abstract = True
