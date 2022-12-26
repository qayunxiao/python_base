# -*- coding: utf-8 -*-
# @Time    : 2022/12/26 9:28
# @Author  : alvin
# @File    : 时间相关.py
# @Software: PyCharm
import time
print("time.localtime",time.localtime(),type(time.localtime()))
currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(currentTime)