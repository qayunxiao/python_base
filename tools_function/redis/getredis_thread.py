# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 19:52
# @Author  : alvin
# @File    : getredis_thread.py
# @Software: PyCharm
import os
from concurrent.futures import  ThreadPoolExecutor
def say_hello():
    print("hello",os.getpid(),end='\n')

exec = ThreadPoolExecutor(20)#线程数量20
for i in range(0,10):
    exec.submit(say_hello)
