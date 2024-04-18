#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/10/11
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['Cipher']

import base64
from abc import ABCMeta

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

from rest_framework_util.core.cipher.backends.base import BaseCipher


class Cipher(BaseCipher):

    def __init__(self, key, model, **kwargs):
        self.encoding = kwargs.pop('encoding', 'utf8')
        self.block_size = 16
        self.key = key.encode(self.encoding)
        self.__cipher = AES.new(key, model, **kwargs)

    @property
    def cipher(self):
        return self.__cipher

    def pad(self, s):
        s = s.encode(self.encoding)
        return pad(s, self.block_size)

    def unpad(self, s):
        return unpad(s, self.block_size)

    def add_16(self, par):
        par = par.encode(self.encoding)
        while len(par) % 16 != 0:
            par += b'\x00'
        return par

    def encrypt_text(self, text):
        encrypted_text = self.cipher.encrypt(self.pad(text))
        return base64.encodebytes(encrypted_text).decode()

    def decrypt_text(self, text):
        text = base64.decodebytes(self.pad(text))
        decrypted_text = self.unpad(self.cipher.decrypt(text))
        return decrypted_text.decode(self.encoding)

    def encrypt(self, file_path, dst_path):
        pass

    def decrypt(self, src_path, dst_path):
        pass

    def is_encrypted(self, file_path):
        pass
