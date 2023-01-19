# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 17:11
# @Author  : alvin
# @File    : getredis.py
# @Software: PyCharm
import  redis
try:
    pool = redis.ConnectionPool(
        host="localhost",
        port=6379,
        password = "",
        db=0,
        max_connections=200
    )
except Exception as e:
    print(e)