#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/10/11
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['cipher', 'ciphers']

from django.core import signals
from django.utils.connection import BaseConnectionHandler, ConnectionProxy
from django.utils.module_loading import import_string

from rest_framework_util.core.cipher.backends.base import InvalidCipherBackendError

DEFAULT_CIPHER_ALIAS = "default"


class CipherHandler(BaseConnectionHandler):
    settings_name = "CIPHERS"
    exception_class = InvalidCipherBackendError

    def create_connection(self, alias):
        params = self.settings[alias].copy()
        backend = params.pop("BACKEND")
        options = params.pop("OPTIONS", {})
        try:
            backend_cls = import_string(f'{backend}.Client')
        except ImportError as e:
            raise InvalidCipherBackendError(
                "Could not find backend '%s': %s" % (backend, e)
            ) from e
        return backend_cls(**options)


ciphers = CipherHandler()

cipher = ConnectionProxy(ciphers, DEFAULT_CIPHER_ALIAS)


def close_ciphers(**kwargs):
    # Some caches need to do a cleanup at the end of a request cycle. If not
    # implemented in a particular backend cache.close() is a no-op.
    ciphers.close_all()


signals.request_finished.connect(close_ciphers)
