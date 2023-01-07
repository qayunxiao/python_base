# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 15:45
# @Author  : alvin
# @File    : role_dao.py
# @Software: PyCharm
from mysql_db import pool
class RoleDao:
    def search_list(self):
        try:
            con  = pool.get_connection()
            cur = con.cursor()
            sql="SELECT id,role from t_role "
            cur.execute(sql )
            res = cur.fetchall()#获取查询结果
            print(res)
            return  res
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()