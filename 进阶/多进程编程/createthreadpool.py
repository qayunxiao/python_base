# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 21:15
# @Author  : alvin
# @File    : createthread.py
# @Software: PyCharm
import time
from concurrent.futures import ThreadPoolExecutor
def work(i):
    print(i)
    time.sleep(1)

if __name__ == '__main__':
    t= ThreadPoolExecutor(2)
    for i in range(20):
        t.submit(work,(i,))
