#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/12/22
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['load_urlpatterns']

from importlib import import_module

from django.conf import settings
from django.urls import path, include


def load_urlpatterns(installed_apps, with_app_prefix=True, user_prefix=None):
    """ 根据installed_apps加载url

    :param list installed_apps: 安装的应用
    :param bool with_app_prefix: 是否以应用名为url前缀
    :param dict user_prefix: 用户自定义url前缀，格式为{‘app名称，即在INSTALL_APP的名称’:'url前缀'}
    :return:
    """
    user_prefix = user_prefix or {}
    _urlpatterns = []
    for no, install_app in enumerate(installed_apps, start=1):
        if settings.MODE == 'app' and not install_app.startswith('rest_framework_admin.'):
            _install_app = install_app + '.app'
        else:
            _install_app = install_app
        _string = f'{_install_app}.urls.urlpatterns'
        print(f'[#{no}] import {_string}')
        try:
            module_path = f'{_install_app}.urls'
            module = import_module(module_path)
            __urlpatterns = getattr(module, 'urlpatterns')
        except ModuleNotFoundError as exc:
            print(f'\t{exc}')
        except ImportError as exc:
            print(f'\t{exc}')
        except BaseException as exc:
            raise exc
        else:
            if with_app_prefix:
                _app_prefix = user_prefix.get(install_app, install_app)
                while _app_prefix.endswith('/'):
                    _app_prefix = _app_prefix[:-1]
                _urlpatterns.append(
                    path(
                        f'{_app_prefix}/',
                        include(module_path)))
            else:
                _urlpatterns += __urlpatterns
        continue
    return _urlpatterns
