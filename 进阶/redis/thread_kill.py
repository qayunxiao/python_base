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
s = set()#集合不能重复
while True:
    if len(s) == 1000:
        break
    num = random.randint(10000,100000)
    s.add(num)
# print(s)

try:
    con.delete("kill_total","kill_num","kill_flag","kill_user")
    con.set("kill_total",50)
    con.set("kill_num",0)
    con.set("kill_flag",1)
    con.expire("kill_flag",600)#设置过期时间10分钟
except Exception as  e:
    print(e)
finally:
    del con

executor = ThreadPoolExecutor(200)

def buy():
    connection = redis.Redis(
            connection_pool=pool
    )
    pipline = connection.pipeline()

    # print(" pipline  in dir ",("pipline" in dir()))
    try:
        if connection.exists("kill_flag") ==1:# 判断秒杀是否结束
            pipline.watch("kill_num" ,"kill_user") #监视键
            total = int(pipline.get("kill_total").decode("utf-8")) #字符串
            num = int(pipline.get("kill_num").decode("utf-8")) #字符串
            if num < total:
                pipline.multi()#开始事物
                pipline.incr("kill_num")#另外事务执行了这个抢购，此时这个是50
                user_id = s.pop() #删除并返回删除内容
                pipline.rpush("kill_user",user_id)
                pipline.execute()#提交事物
    except Exception as e:
        print("Exception",e)
    finally:
        if "pipline" in dir():
            pipline.reset() #关闭链接
        del connection

for i in range(0,1000):
    executor.submit(buy)
print("秒杀结束")