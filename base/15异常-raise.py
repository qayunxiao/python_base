# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 14:18
# @Author  : alvin
# @File    : 15异常.py
# @Software: PyCharm

class NewError(Exception):
    def __init__(self,mess):
        self.mess=mess

def qatest():
    raise NewError('new error')

try:
    qatest()
except Exception as e:
    print(e)
qatest()