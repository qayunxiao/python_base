# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 9:21
# @Author  : alvin
# @File    : 异步.py
# @Software: PyCharm
import os
import random
import time
import asyncio

async def a():
    for i in range(10):
        print(i,"a",os.getpid())
        #time.sleep cpu级别的阻塞
        await  asyncio.sleep(random.random() *2)
    return  'a func'


async def b():
    for i in range(10):
        print(i,"b",os.getpid())
        await  asyncio.sleep(random.random() *2)
    return  'b func'

async def main():
    res =await  asyncio.gather(
        a(),
        b()
    )
    print(res[0],res[1])

if __name__ == '__main__':
    start=time.time()
    asyncio.run(main())
    # a()
    # b()
    print("time is:{}".format(time.time() - start),os.getpid())