#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2024/1/4
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['FileView']

from typing import NamedTuple


class FileView(NamedTuple):
    # 最终的存储路径为{dir_path}/{随机id}.{文件格式}
    # 文件类型
    file_type: str
    # 当分片时，用于创建临时文件夹
    file_id: str
    # 文件目录（自定义）,上传到minio时的prefix
    dir_path: str
    # 任务id
    task_id: str
    # 分片序号，-1表示不分片
    chunk: int
    # 分片上传成功后使用
    file_name: str
