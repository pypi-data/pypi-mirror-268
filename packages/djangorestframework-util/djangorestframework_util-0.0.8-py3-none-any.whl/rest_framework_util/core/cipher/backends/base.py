#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/10/11
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['BaseCipher', 'InvalidCipherBackendError']

from abc import ABC, abstractmethod

from django.core.exceptions import ImproperlyConfigured


class BaseCipher(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def encrypt(self, file_path, dst_path):
        pass

    @abstractmethod
    def decrypt(self, src_path, dst_path):
        pass

    @abstractmethod
    def is_encrypted(self, file_path):
        pass


class InvalidCipherBackendError(ImproperlyConfigured):
    pass
