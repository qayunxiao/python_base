# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 19:33
# @Author  : alvin
# @File    : 投票案例.py
# @Software: PyCharm
import time

import  redis
from redispool import pool
import  random

con = redis.Redis(
    connection_pool=pool
)
try:
    print("exists",con.exists("ballot"))
    if con.exists("ballot"):
        print("存在就删除")
        con.delete("ballot")
    con.zadd("ballot",{"马云":0,"丁磊":0,"马化腾":0,"李彦宏":0,"张朝阳":0})
    names = ["马云" ,"丁磊" ,"马化腾" ,"李彦宏" ,"张朝阳" ]
    for i in range (0,300):
        num = random.randint(0,4)
        name = names[num]
        con.zincrby("ballot",1,name)
    res = con.zrevrange("ballot",0,-1,"WITHSCORES")#WITHSCORES分数值
    for i in res:
        print(i[0].decode("utf-8"),int(i[1]))

except Exception as e:
    print(e)
finally:
    del con