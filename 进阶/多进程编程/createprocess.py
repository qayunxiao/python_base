# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 15:28
# @Author  : alvin
# @File    : createprocess.py
# @Software: PyCharm
import time
import os
import multiprocessing
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
    a_p = multiprocessing.Process(target=work_a )#子进程1
 #   a_p.start()
    # work_a()
    b_p=multiprocessing.Process(target=work_b)#子进程2
#    b_p.start()
    for p in (a_p,b_p):
        p.start()
    print("时间消耗",time.time()-start) #主进程
    print("parent pid is {}".format(os.getpid()))