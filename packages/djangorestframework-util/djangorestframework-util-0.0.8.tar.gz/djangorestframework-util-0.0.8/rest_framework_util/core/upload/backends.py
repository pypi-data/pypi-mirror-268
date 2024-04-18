#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2024/1/4
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['upload', 'merge']

import os
import shutil
import tempfile
from io import BytesIO

import cv2
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from rest_framework_util.core.upload import FileView
from rest_framework_util.core.upload.settings import UploadSettings
from rest_framework_util.core.upload.configs import FileTypeEnum
from shortcut_util.unique import uuid_id


def __tmp_dir():
    return tempfile.TemporaryDirectory(
        prefix=f'{settings.APP_CODE}__', dir='/tmp')


def __upload(request, file_view, file_obj, app_settings):
    if app_settings.save_original_name:
        file_name = os.path.basename(file_obj.name)
    else:
        file_name = uuid_id() + '.' + file_obj.name.rsplit(".")[-1]
    if file_view.file_type == FileTypeEnum.video.name:
        dst_path = f'{file_view.dir_path}/{file_name}'
        app_settings.storage.upload_file(file_obj, dst_path)
        url = app_settings.storage.to_http(dst_path, request=request)
        # 获取关键帧作为封面
        with __tmp_dir() as tmp_dir:
            file_path = os.path.join(tmp_dir, file_name)
            file_obj.seek(0, 0)
            with open(file_path, 'wb') as fd:
                fd.write(file_obj.read())
            cap = cv2.VideoCapture(file_path)
            cap.set(cv2.CAP_PROP_POS_FRAMES, 10)  # keys_frame为关键帧的序号
            flag, frame = cap.read()  # frame为关键帧图片，Mat类型
            poster = ""
            if flag:
                img = cv2.resize(frame, None, fx=0.5, fy=0.5)
                # 保存图片质量改为75
                encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 75]
                result, encimg = cv2.imencode('.jpg', img, encode_param)
                img = BytesIO(encimg)
                file_name = file_view.task_id + ".jpg"  # 文件保存名称
                dst_path = f'{file_view.dir_path}/{file_view.task_id}/{file_name}'
                app_settings.storage.upload_file(img, dst_path)
                url = app_settings.storage.to_http(dst_path, request=request)
            cap.release()
        return {"path": url, "poster": poster}
    elif file_view.file_type == FileTypeEnum.file.name:
        _, file_ext = os.path.splitext(file_obj.name)
        if file_ext in app_settings.cipher_file_type_exts and app_settings.cipher:
            # 解密文件
            with __tmp_dir() as tmp_dir:
                file_path = os.path.join(tmp_dir, file_name)
                encrypted_file_path = file_path + '.enc'
                decrypted_file_path = file_path + '.dec'
                # 将上传的文件保存到本地
                with open(encrypted_file_path, "wb+") as encrypted_fd:
                    encrypted_fd.write(file_obj.read())
                if app_settings.cipher.is_encrypted(encrypted_file_path) == 0:
                    # 解密
                    return_code = app_settings.cipher.decrypt(
                        encrypted_file_path, decrypted_file_path)
                    if return_code != 0:
                        raise ValidationError(f'文件解密失败，code={return_code}.')
                else:
                    decrypted_file_path = encrypted_file_path
                with open(decrypted_file_path, 'rb') as fd:
                    dst_path = f'{file_view.dir_path}/{file_name}'
                    app_settings.storage.upload_file(fd, dst_path)
                    url = app_settings.storage.to_http(dst_path, request=request)
        else:
            dst_path = f'{file_view.dir_path}/{file_name}'
            app_settings.storage.upload_file(file_obj, dst_path)
            url = app_settings.storage.to_http(dst_path, request=request)
    elif file_view.file_type == FileTypeEnum.image.name:
        _, file_ext = os.path.splitext(file_obj.name)
        if file_ext in app_settings.image_type_exts:
            dst_path = f'{file_view.dir_path}/{file_name}'
            app_settings.storage.upload_file(file_obj, dst_path)
            url = app_settings.storage.to_http(dst_path, request=request)
        else:
            raise ValidationError(f'图像格式错误[{file_ext}]')
    else:
        raise ValidationError(f'不支持的文件类型[{file_view.file_type}]')
    return {"path": url}


def upload(request, file_view, file_obj, app_settings):
    """ 上传文件的请求

    :param Request request: Request
    :param FileView file_view: 文件信息
    :param IO file_obj: 文件对象
    :param UploadSettings app_settings: 配置
    :return: Response
    :rtype: Response
    """
    if not file_obj:
        raise ValidationError(_('文件无效'))
    if file_view.chunk == -1:
        # 不分片，直接上传
        data = __upload(request, file_view, file_obj, app_settings)
        return Response(data)
    else:
        # 分片，保存本地
        file_path = os.path.join(
            app_settings.tmp_upload_dir,
            file_view.file_id,
            file_view.chunk)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as fd:
            fd.write(file_obj.file.read())
        return Response()


def merge(request, file_view, app_settings):
    """ 合并文件的请求（所有分片均上传完后被调用）

    :param request: Request
    :param FileView file_view: 文件信息
    :param UploadSettings app_settings: 上传配置
    :return: Response
    """
    dir_path = os.path.join(app_settings.tmp_upload_dir, file_view.file_id)
    if not (os.path.exists(dir_path) and os.path.isdir(dir_path)):
        raise ValidationError('分片文件不存在')
    file_path = os.path.join(dir_path, file_view.file_name)
    try:
        with open(file_path, 'ab') as fd:
            chunk = 0  # 分片序号
            while True:
                chunk_file_path = os.path.join(dir_path, chunk)
                if os.path.exists(chunk_file_path) and os.path.isfile(
                        chunk_file_path):
                    with open(chunk_file_path, 'rb') as chunk_fd:
                        fd.write(chunk_fd.read())
                    chunk += 1
                else:
                    break
        with open(file_path, 'rb') as fd:
            data = __upload(request, file_view, fd, app_settings)
        return Response(data=data)
    except BaseException:
        raise ValidationError('文件合并错误')
    finally:
        shutil.rmtree(dir_path)
