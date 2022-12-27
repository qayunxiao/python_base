# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 22:11
# @Author  : alvin
# @File    : 目录操作.py
# @Software: PyCharm
import os
#获取当前目录
print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))

#获取全路径与文件名
print(os.path.abspath(__file__))

#获取上一级目录名称
print(os.path.dirname(os.getcwd()))

#路径拼接
# os.path.join(os.path.dirname(os.getcwd()),'case')
print(os.path.join(os.path.dirname(os.getcwd()),"base"))
print(os.path.join(os.getcwd(),'dir.py'))
print(os.path.join(os.getcwd(),'unittest','dir.py'))
