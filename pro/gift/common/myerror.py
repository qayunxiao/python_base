# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 19:52
# @Author  : alvin
# @File    : error.py
# @Software: PyCharm

class NotPathError(Exception):
    def __init__(self,message):
        self.message = message

class FormatError(Exception):
    def __init__(self,message='need json format'):
        self.message =message
class NotFileError(Exception):
    def __init__(self,message='this is not file'):
        self.messsage = message


class UserExistsError(Exception):
    def __init__(self,message='user is exits'):
        self.message = message

class RoleError(Exception):
    def __init__(self,message='角色不正确'):
        self.meassage = message
class LevelError(Exception):
    def __init__(self,message='等级不对'):
        self.message = message
