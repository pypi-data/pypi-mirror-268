#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['get_logging_config']

import os
from pathlib import Path


def get_logging_config(log_dir, log_level):
    if isinstance(log_dir, Path):
        log_dir = log_dir.as_posix()
    os.makedirs(log_dir, exist_ok=True)
    log_class = 'shortcut_util.log.TimedRotatingFileHandler'
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {},
        'formatters': {
            'default': {
                "format": (
                    "[%(asctime)s] %(pathname)s "
                    "%(lineno)d %(process)d %(thread)d "
                    "%(levelname)s %(message)s"
                ),
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        'handlers': {
            'root': {
                "class": log_class,
                "formatter": "default",
                "filename": os.path.join(log_dir, 'root.log'),
                # "maxBytes": 1024 * 1024 * 10,
                "backupCount": 10,
            },
            'console': {
                'level': log_level,
                'class': 'logging.StreamHandler',
                "formatter": "default",
            },
            "mysql": {
                "class": log_class,
                "formatter": "default",
                "filename": os.path.join(log_dir, 'mysql.log'),
                "backupCount": 10,
            },
            "django": {
                "class": log_class,
                "formatter": "default",
                "filename": os.path.join(log_dir, 'django.log'),
                "backupCount": 10,
            },
        },
        'loggers': {
            'root': {
                'handlers': ['root'],
                'level': log_level,
            },
            'console': {
                'handlers': ['console'],
                'level': log_level,
                'propagate': False,
            },
            "django": {
                "handlers": ['django', 'console'],
                "level": log_level,
                "propagate": False
            },
            "django.db.backends": {
                "handlers": ["mysql"],
                # 通过设置level来调整sql的输出
                "level": log_level,
                "propagate": False,
            },
        }
    }
    return config
