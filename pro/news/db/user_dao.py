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
    #创建用户
    def insert_user(self,username,password,email,role_id):
        try:
            con  = pool.get_connection()
            con.start_transaction()#开始事务
            cur = con.cursor()
            sql="INSERT INTO t_user(username,password,email,role_id)" \
                "VALUES (%s,HEX(AES_ENCRYPT(%s,'HelloWorld')),%s,%s)"
            # print("search_unreview_list sql",sql)
            cur.execute(sql,(username,password,email,role_id))
            con.commit()
        except Exception as e:
            print(e)
            if "con" in dir():
                con.rollback()
        finally:
            if "con" in dir():
                con.close()

    def search_user_count(self):
        try:
            con  = pool.get_connection()
            cur = con.cursor()
            sql="SELECT COUNT(*) from t_user "
            cur.execute(sql)
            res = cur.fetchone()[0]#获取查询结果
            return  res
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    #用户列表
    def search_user_list(self,page):
        try:
            con  = pool.get_connection()
            cur = con.cursor()
            sql="SELECT u.id,u.username,r.role " \
                "FROM t_user u JOIN t_role r " \
                "ON u.role_id=r.id " \
                "ORDER BY u.id DESC " \
                "LIMIT %s,%s"
            # print("search_user_list sql",sql)
            cur.execute(sql,((page-1)*10,10))
            res = cur.fetchall()
            return  res
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def update(self,id,username,password,email,role_id):
        # print("dao user",id,username,password,email,role_id)
        try:
            con  = pool.get_connection()
            con.start_transaction()#开始事务
            cur = con.cursor()
            sql="UPDATE t_user SET username=%s," \
                "password=HEX(AES_ENCRYPT(%s,'HelloWorld'))," \
                "email = %s, role_id= %s WHERE id =%s "

            cur.execute(sql,(username,password,email,role_id,id))
            # print("update user sql",sql,(username,password,email,role_id,id))
            con.commit()
        except Exception as e:
            print(e)
            if "con" in dir():
                con.rollback()
        finally:
            if "con" in dir():
                con.close()
    #删除用户
    def delete_by_id(self,id ):
        try:
            con  = pool.get_connection()
            con.start_transaction()#开始事务
            cur = con.cursor()
            sql=" DELETE FROM t_user WHERE id={} "
            cur.execute(sql.format(id))
            con.commit()
        except Exception as e:
            print(e)
            if "con" in dir():
                con.rollback()
        finally:
            if "con" in dir():
                con.close()


if __name__ == '__main__':
    a=UserDao()
    # t=a.login(username="alvin",password="qatest")
    # t2=a.search_user_role(username="alvin")
    t3=a.search_user_list(page=2)
    print(t3)
    #username,password,email,role_id,id
    # t4=a.update("wangalvin","123","qa@q.com",1,16)
    # print(t4)