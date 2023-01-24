# -*- coding: utf-8 -*-
# @Time    : 2023/1/24 9:25
# @Author  : alvin
# @File    : r14todb.py
# @Software: PyCharm
import xlrd
import mysql.connector
config={
    "host":"127.0.0.1",
    "port":3306,
    "user":"qa",
    "password":"qatest",
    "database":"bdh14"
}
con = mysql.connector.connect(**config)

excel = xlrd.open_workbook("2022年基本田资格补贴情况统计表(14).xlsx")
#获取工作簿
book = excel.sheet_by_name("Sheet1")
print(book.get_rows())

content = []
for i in book.get_rows():
    datainfo = []
    for j in i:
        if isinstance(j.value,float):
            datainfo.append(int(j.value))
        else:
            datainfo.append(j.value)
    # print(datainfo)
    content.append(tuple(datainfo))

# print(content)


# "
for i in content:
    # print(i)
    sql1='INSERT into record (id,address,name,kyc,yhk,amount,tel,year) VALUES {}'.format(i)
    print(sql1)
    cur = con.cursor()
    cur.execute(sql1)
    con.commit()#提交
con.close()