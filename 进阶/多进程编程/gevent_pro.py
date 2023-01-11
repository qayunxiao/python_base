# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 16:36
# @Author  : alvin
# @File    : gevent_pro.py
# @Software: PyCharm
import os
import random
import time
import asyncio
import gevent

def gevent_a():
    for i in range(10):
        print(i,'a.text gevent',os.getpid())
        gevent.sleep(random.random() *2)
    return 'gevent a.text reslut'
def gevent_b():
    for i in range(10):
        print(i,'b gevent',os.getpid())
        gevent.sleep(random.random() *2)
    return 'gevent b reslut'

async def a():
    for i in range(10):
        print(i,"a.text",os.getpid())
        #time.sleep cpu级别的阻塞
        await  asyncio.sleep(random.random() *2)
    return  'a.text func'


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
    # asyncio.run(main())
    # a.text()
    # b()

    g_a = gevent.spawn(gevent_a)
    g_b = gevent.spawn(gevent_b)
    gevent_list = [g_a,g_b]
    res = gevent.joinall(gevent_list)
    # print(dir(res))
    print(res[0].value)
    print(res[1].value)


print("time is:{}".format(time.time() - start),os.getpid())