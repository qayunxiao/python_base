# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 17:41
# @Author  : alvin
# @File    : getredis_list.py
# @Software: PyCharm
import  redis
from redispool import  pool

try:
    con = redis.Redis(
        connection_pool=pool
    )
    con.rpush("pydname","董事会","秘书处","财务部","技术部")
    con.lpop("pydname")
    res = con.lrange("pydname" ,0,-1)
    for i in res:
        print(i.decode("utf-8"))
except Exception as  e:
    print(e)
finally:
    del con