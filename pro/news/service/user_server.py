# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 9:34
# @Author  : alvin
# @File    : user_server.py
# @Software: PyCharm
from user_dao import UserDao
#service 写业务逻辑
class UserService:
    __user_dao = UserDao()
    def login(self,username,password):
        print("service user",username,password)
        res=self.__user_dao.login(username,password)
        return res
    #查询用户角色
    def search_user_role(self,username):
        role = self.__user_dao.search_user_role(username)
        return role
     #添加记录
    def insert_user(self,username,password,email,role_id):
        self.__user_dao.insert_user(username,password,email,role_id)

    def search_user_count(self):
        page_user=self.__user_dao.search_user_count()
        return page_user

    def search_user_list(self,page):
        res=self.__user_dao.search_user_list(page)
        return res
    #   修改用户
    def update(self,id,username,password,email,role_id):
        self.__user_dao.update(id,username,password,email,role_id)
        #删除用户
    def delete_by_id(self,id):
        self.__user_dao.delete_by_id(id)