# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 15:48
# @Author  : alvin
# @File    : role_service.py
# @Software: PyCharm
from role_dao import RoleDao

class RoleService:
    __role_dao = RoleDao()

    def search_list(self):
        res = self.__role_dao.search_list()
        return res