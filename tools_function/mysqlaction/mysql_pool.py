# -*- coding: utf-8 -*-
# @Time    : 2023/1/6 10:01
# @Author  : alvin
# @File    : mysql_pool.py
# @Software: PyChar
"""
使用DBUtils数据库连接池中的连接，操作数据库
OperationalError: (2006, ‘MySQL server has gone away’)
"""
import mysql.connector.pooling
confing={
    "host":"127.0.0.1",
    "port":3306,
    "user":"qa",
    "password":"qatest",
    "database":"jmeter"
}
    try:
    # 创建连接池
    pool=mysql.connector.pooling.MySQLConnectionPool(
        **confing,
        pool_size=10
    )
    #获取连接池
    con = pool.get_connection()
    con.start_transaction()
    cur = con.cursor()
    sql ="update order_pay set total_amount=total_amount+%s WHERE id =%s"
    cur.execute(sql,(10,21))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()#回
    print(e)

