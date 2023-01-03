# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 19:51
# @Author  : alvin
# @File    : base.py
# @Software: PyCharm
import os
from common import error
from common.utils import check_file
class Base(object):
    def __init__(self,user_json,gift_json):
        self.user_json= user_json
        self.gift_json= gift_json
        self.__check_user_json()
        self.__check_gift_json()

    def __check_user_json(self):
        check_file(self.user_json)
    def __check_gift_json(self):
        check_file(self.gift_json)

if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(),"storage","gift.json")
    user_path = os.path.join(os.getcwd(),"storage","user.json")
    print(gift_path,user_path)
    base=Base(user_json=user_path,gift_json=gift_path)

