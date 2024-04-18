#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2024/1/4
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['UploadSettings']

from rest_framework_util.core.storage import storage


class UploadSettings:
    # 是否保留原始名称
    save_original_name = False
    # 图像类型文件支持的扩展名
    image_type_exts = (
        '.jpg',
        '.jpeg',
        '.gif',
        '.png',
        '.bmp',
        '.webp',
        '.svg',
        '.icon',
        '.tif')
    # 文件类型文件支持加解密的扩展名
    cipher_file_type_exts = (
        '.parquet',
        '.csv',
        '.tsv',
        '.xls',
        '.xlsx')
    # 分片文件临时保存目录
    tmp_upload_dir = '/tmp/',
    # 存储客户端
    storage = storage
    # 加密
    cipher = None
