# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 19:58
# @Author  : alvin
# @File    : thread_kill.py
# @Software: PyCharm
import redis
from redispool import pool
import  random
from concurrent.futures import  ThreadPoolExecutor
con=redis.Redis(
    connection_pool=pool
)
s = set()
while True:
    if len(s) == 1000:
        break
    num = random.randint(10000,100000)
    s.add(num)
print(s)

try:
    con.delete("kill_total","kill_num","kill_flag","kill_user")
except Exception as  e:
    print(e)
finally:
    del con

exec = ThreadPoolExecutor(200)
def buy():
    pass