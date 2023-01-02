# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 16:19
# @Author  : alvin
# @File    : processlock.py
# @Software: PyCharm

from  multiprocessing import  Manager
import multiprocessing
import os
import time

def work(count,lock):
    lock.acquire()
    print(count,os.getpid())
    time.sleep(5)
    lock.release()#释放锁
    return 'res is {},pid is {}'.format(count,os.getpid())

if __name__ == '__main__':
    pool = multiprocessing.Pool(5)#创建为5的进程池
    manage = Manager()
    lock = manage.Lock()
    results =[]
    for i in range(20):
        #lock作为参数传入
        result=pool.apply_async(func=work,args=(i,lock))
        # results.append(result)
    pool.close()
    pool.join()#等子进程结束之后再主进程结束，保证进程池任务全部结束再退出主进程
    # for _results in results:
    #     print(_results.get())

