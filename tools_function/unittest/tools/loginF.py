# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 19:29
# @Author  : alvin
# @File    : loginF.py
# @Software: PyCharm

def loginf(username,password):
    if username == "admin" and password == "password":
        return "登录成功"
    else:
        return "登录失败"