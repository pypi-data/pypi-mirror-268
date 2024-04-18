#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['login_exempt', 'login_exempt_func', 'is_login_exempt']

from functools import wraps


def login_exempt(view_func):
    """Mark a view function as being exempt from login view protection"""

    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)
    wrapped_view.login_exempt = True
    return wraps(view_func)(wrapped_view)


def login_exempt_func(view_func, func=None):
    """ 自定义是否排除登录校验
    :param view_func: view试图
    :param func: 回调方法，接收一个request对象
    """

    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)
    wrapped_view.login_exempt_func = func
    return wraps(view_func)(wrapped_view)


def is_login_exempt(request, view):
    _login_exempt = getattr(view, "login_exempt", False)
    if _login_exempt:
        return True
    _login_exempt_func = getattr(view, "login_exempt_func", None)
    if _login_exempt_func is None:
        return False
    try:
        return _login_exempt_func(request, view)
    except BaseException:
        return False
