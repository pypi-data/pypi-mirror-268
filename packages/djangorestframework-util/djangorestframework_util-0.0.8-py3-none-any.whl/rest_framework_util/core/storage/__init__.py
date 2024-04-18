#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['storage', 'storages']

from django.core import signals
from django.utils.connection import BaseConnectionHandler, ConnectionProxy
from django.utils.module_loading import import_string

from rest_framework_util.core.storage.backends.base import InvalidStorageBackendError

DEFAULT_STORAGE_ALIAS = "default"


class StorageHandler(BaseConnectionHandler):
    settings_name = "STORAGES"
    exception_class = InvalidStorageBackendError

    def create_connection(self, alias):
        params = self.settings[alias].copy()
        backend = params.pop("BACKEND")
        options = params.pop("OPTIONS", {})
        try:
            backend_cls = import_string(f'{backend}.Client')
        except ImportError as e:
            raise InvalidStorageBackendError(
                "Could not find backend '%s': %s" % (backend, e)
            ) from e
        return backend_cls(**options)


storages = StorageHandler()

storage = ConnectionProxy(storages, DEFAULT_STORAGE_ALIAS)


def close_storages(**kwargs):
    # Some caches need to do a cleanup at the end of a request cycle. If not
    # implemented in a particular backend cache.close() is a no-op.
    storages.close_all()


signals.request_finished.connect(close_storages)
