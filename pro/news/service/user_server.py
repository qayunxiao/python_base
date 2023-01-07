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