# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 9:10
# @Author  : alvin
# @File    : mysql_db.py
# @Software: PyCharm
import  mysql.connector.pooling
# 私有变量
__config ={
    "host":"localhost",
    "port":3306,
    "user":"qa",
    "password":"qatest",
    "database":"vega"
}
try:
    pool=mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
except Exception as e:
    print(e)