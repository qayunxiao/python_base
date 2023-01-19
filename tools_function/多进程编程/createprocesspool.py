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
    return 'res is {},pid is {}'.format(count,os.getpid())

if __name__ == '__main__':
    pool = multiprocessing.Pool(5)#创建为5的进程池
    results =[]
    for i in range(20):
        result=pool.apply_async(func=work,args=(i,))
        results.append(result)
    # pool.close()
    # pool.join()#等子进程结束之后再主进程结束，保证进程池任务全部结束再退出主进程
    for _results in results:
        print(_results.get())