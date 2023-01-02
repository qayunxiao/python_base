# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 21:15
# @Author  : alvin
# @File    : createthread.py
# @Software: PyCharm
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
lock = threading.Lock()
def work(i):
    # lock.acquire()
    print(os.getpid())
    time.sleep(1)
    # lock.release(
    return  'res is {}'.format(i)

if __name__ == '__main__':
    print(os.getpid())
    t= ThreadPoolExecutor(2)
    res=[]
    for i in range(20):
        t_res=t.submit(work,(i,))
        res.append(t_res)

    for _res in res:
        print(_res.result())