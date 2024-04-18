#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['APISettings', 'get_api_settings']

from django.conf import settings
from django.core.signals import setting_changed
from rest_framework.settings import APISettings as _APISettings

DEFAULTS = []
REMOVED_SETTINGS = []
IMPORT_STRINGS = []


class APISettings(_APISettings):
    def __init__(self, settings_key, user_settings=None,
                 defaults=None, import_strings=None, doc_url=None):
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or DEFAULTS
        self.import_strings = import_strings or IMPORT_STRINGS
        self._cached_attrs = set()
        self.settings_key = settings_key
        self.doc_url = doc_url

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, self.settings_key, {})
        return self._user_settings

    def __check_user_settings(self, user_settings):
        for setting in REMOVED_SETTINGS:
            if setting in user_settings:
                raise RuntimeError(
                    "The '%s' setting has been removed. Please refer to '%s' for available settings." %
                    (setting, self.doc_url))
        return user_settings


def get_api_settings(settings_key, *args, **kwargs):
    def reload_api_settings(*_args, **_kwargs):
        setting = kwargs['setting']
        if setting == settings_key:
            api_settings.reload()
    api_settings = APISettings(settings_key, *args, **kwargs)
    setting_changed.connect(reload_api_settings)
    return api_settings
