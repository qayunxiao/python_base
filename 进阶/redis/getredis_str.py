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
con.set("country","英国")
# con.set("city","伦敦")
# city = con.get("city").decode("utf-8")
con.expire("city",5)
time.sleep(6)
city = con.get("city").decode("utf-8")
print(city)

# del con