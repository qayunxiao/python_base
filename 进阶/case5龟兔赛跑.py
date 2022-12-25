# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 10:28
# @Author  : alvin
# @File    : case5龟兔赛跑.py
# @Software: PyCharm
import time
import random
track_length = 10
def runtime (func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(func.__name__,"运行时间是",end_time-start_time,"秒")
    return wrapper
@runtime
def torroise():
    # for i in [1,2,3,4,5,6,7,8,9,10]:
    for i in range(1,track_length+1):
        print("乌龟爬的{}米".format(i))
        time.sleep(1)

@runtime
def rabbit():
    # for i in [1,2,3,4,5,6,7,8,9,10]:
    for i in range(1,track_length+1):
        if i % 5 == 0:
            time.sleep(random.randint(1,10))
        print("兔子的{}米".format(i))
torroise()
rabbit()