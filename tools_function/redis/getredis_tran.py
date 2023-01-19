# -*- coding: utf-8 -*-
# @Time    : 2023/1/5 19:21
# @Author  : alvin
# @File    : getredis_tran.py
# @Software: PyCharm
import time

import  redis
from redispool import pool

con = redis.Redis(
    connection_pool=pool
)
try:
    pipline = con.pipeline()
    pipline.watch("9527")
    pipline.multi()#开启事物
    pipline.hset("9527","name","alvin")
    pipline.hset("9527","age",30)
    time.sleep(10)
    pipline.execute() #没执行之前，如果9527被修改则不会提交 保持事务一致性
except Exception as e:
    print(e)
finally:
    if "pipline" in dir():
        pipline.reset()
    del con