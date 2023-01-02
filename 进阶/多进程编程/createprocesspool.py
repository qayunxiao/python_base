# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 16:01
# @Author  : alvin
# @File    : createprocesspool.py
# @Software: PyCharm
import multiprocessing
import os
import time

def work(count):
    print(count,os.getpid())
    time.sleep(5)

if __name__ == '__main__':
    pool = multiprocessing.Pool(5)#创建为5的进程池
    for i in range(20):
        pool.apply_async(func=work,args=(i,))
    time.sleep(20)