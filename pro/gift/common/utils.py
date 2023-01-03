# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 19:51
# @Author  : alvin
# @File    : utils.py
# @Software: PyCharm
import os
from .error import NotFileError,FormatError,NotPathError

def check_file(path):
    if not os.path.exists(path):
        raise NotPathError('NOT Found :{}'.format(path))
    if not path.endswith('.json'):
        raise FormatError("need json format")
    if not  os.path.isfile(path):
        raise NotFileError()