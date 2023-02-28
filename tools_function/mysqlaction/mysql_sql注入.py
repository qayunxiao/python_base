# -*- coding: utf-8 -*-
# @Time    : 2023/1/6 11:08
# @Author  : alvin
# @File    : mysql_sql注入.py
# @Software: PyCharm

import  mysql.connector
confing={
    "host":"127.0.0.1",
    "port":3306,
    "user":"qa",
    "password":"qatest",
    "database":"jmeter"
}
con = mysql.connector.connect( **confing )
username =  "1 OR True"
password = "1 OR 1=1"
sql="SELECT count(*) from user WHERE username=%s and AES_DECRYPT(UNHEX(password),'hellowworld') = %s"
sql2="SELECT count(*) from user WHERE username={} and AES_DECRYPT(UNHEX(password),'hellowworld') = {}".format(username,password)

print(sql,sql2)
cur = con.cursor()
# cur.execute(sql%(username,password))
# cur.execute(sql2.format(username,password))
cur.execute(sql,(username,password)) #预编译防止sql注入
print(cur.fetchall()[0])
con.close()