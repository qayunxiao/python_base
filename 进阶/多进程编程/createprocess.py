# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 15:28
# @Author  : alvin
# @File    : createprocess.py
# @Software: PyCharm
import time
import os
def work_a():
    for i in range(10):
        print(i,'a',os.getpid())
        time.sleep(1)

def work_b():
    for i in range(10):
        print(i,'b',os.getpid())
        time.sleep(1)

if __name__ == '__main__':
    start=time.time()
    work_a()
    work_b()
    print(time.time()-start)
    print("parent pid is {}".format(os.getpid()))