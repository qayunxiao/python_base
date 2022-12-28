# -*- coding: utf-8 -*-
# @Time    : 2022/12/26 9:28
# @Author  : alvin
# @File    : 时间相关.py
# @Software: PyCharm
#导入包
import datetime
print(datetime.datetime.now())# 当前时间

from datetime import timedelta
now = datetime.datetime.now()
three_days= timedelta(days=3)#3天对象
after_three_day = now + three_days #获取3天以后对象
after_three_day_str=after_three_day.strftime('%Y-%m-%d %H:%M:%S')
print(after_three_day)
#时间对象转字符串
print(type(now))
now = datetime.datetime.now()
str_date=now.strftime("%Y-%m-%d %H:%M:%S")
print(str_date,type(str_date))

import time
print("time.localtime",time.localtime(),type(time.localtime()))
currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(time.time())#浮点时间戳 秒级别的
print(time.localtime())#获取本地时间函数
print(time.sleep(3))
time_obj = time.strptime("2022-12-28",'%Y-%m-%d')
print(datetime.datetime.timestamp(datetime.datetime.now()))#
print(time.time())#浮点时间戳 秒级别的
print(time.time() * 1000)#浮点时间戳 毫秒级别的
print(datetime.datetime.fromtimestamp(time.time()))
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))



