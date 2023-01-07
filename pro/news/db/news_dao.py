# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 10:23
# @Author  : alvin
# @File    : news_dao.py
# @Software: PyCharm
from  mysql_db import  pool

class NewsDao:
    #查询带审批列表
    def search_unreview_list(self,page):
        try:
            con  = pool.get_connection()
            cur = con.cursor()
            sql="SELECT n.id,n.title,t.type,u.username " \
                "FROM t_news n JOIN t_type t ON n.type_id = t.id " \
                "JOIN t_user u ON n.editor_id=u.id " \
                "WHERE n.state=%s " \
                "ORDER BY n.id DESC " \
                "LIMIT %s,%s"
            # print("search_unreview_list sql",sql)
            cur.execute(sql,("待审批",(page-1)*10,10))
            res = cur.fetchall()
            return  res
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    #查询待审批总页数
    def search_unreview_count_page(self):
        try:
            con  = pool.get_connection()
            cur = con.cursor()
            sql="SELECT COUNT(*) from t_news N WHERE n.state=%s"
            cur.execute(sql,["待审批"])
            res = cur.fetchone()[0]#获取查询结果
            return  res
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

if __name__ == '__main__':
    new=NewsDao()
    res=    new.search_unreview_list(1)
    print(res)