# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 9:15
# @Author  : alvin
# @File    : user_dao.py
# @Software: PyCharm
from mysql_db import pool

class UserDao:

    def login(self,username,password):
        try:
            con  = pool.get_connection()
            cur = con.cursor()
            sql="SELECT COUNT(*) FROM t_user WHERE username=%s AND " \
                "AES_DECRYPT(UNHEX(password),'HelloWorld')=%s"
            cur.execute(sql,(username,password))
            count = cur.fetchone()[0]
            # print("count",count)
            return  True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #查询用户角色
    def search_user_role(self,username):
        try:
            con  = pool.get_connection()
            cur = con.cursor()
            sql="SELECT r.role FROM t_user u JOIN t_role r ON u.role_id = r.id " \
                "WHERE username=%s "
            # print("search sql",sql)
            cur.execute(sql,[username])
            role = cur.fetchone()[0]
            return  role
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

if __name__ == '__main__':
    a=UserDao()
    t=a.login(username="alvin",password="qatest")
    t2=a.search_user_role(username="alvin")
    print(t2)