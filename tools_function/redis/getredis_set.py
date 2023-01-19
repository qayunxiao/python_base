# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 17:47
# @Author  : alvin
# @File    : getredis_set.py
# @Software: PyCharm
import  redis
from redispool import  pool
try:
    con = redis.Redis(
        connection_pool=pool
    )
    con.sadd("employees",8001,8002,8003)
    con.srem("employees",8002)
    res = con.smembers("employees")
    for i in res:
        print(i.decode("utf-8"))
    con.zadd("keywords",{"马云":0,"张朝阳":0,"丁磊":0})#添加有序集合
    con.zincrby("keywords",10,"马云")#马云加10
    con.zincrby("keywords",11,"张朝阳")#马云加10
    res1 = con.zrevrange("keywords",0,-1)
    for one in res1:
        print(one.decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con
