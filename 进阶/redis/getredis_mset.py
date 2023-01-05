# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 17:11
# @Author  : alvin
# @File    : getredis.py
# @Software: PyCharm
import time

import redis
from redispool import pool

con = redis.Redis(
    connection_pool=pool
)
try:
    con.delete("country","city")
    con.mset( {"country":"德国","city":"伦敦"} )
    res = con.mget(("country","city")) #元祖
    for i in res:
        print(i.decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con

    # del con