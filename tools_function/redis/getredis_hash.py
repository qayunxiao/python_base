# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 18:55
# @Author  : alvin
# @File    : getredis_hash.py
# @Software: PyCharm
import redis
from redispool import  pool
try:
    con = redis.Redis(
        connection_pool=pool
    )
    con.hset("9527","city","纽约")
    con.hset("9527","sex","male")
    con.hset("9527","age","45")
    con.hdel("9527","age")
    res1=con.exists("9527","name")
    print(res1)
    res = con.hgetall("9527")
    for i in res:
        print(i.decode("utf-8"),res[i].decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con