# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 19:51
# @Author  : alvin
# @File    : base.py
# @Software: PyCharm
import json
import os
import time

from common.utils import check_file,timestamp_to_string
from common  import myerror
from common.consts import ROLES
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

    def __read_users(self,time_str=False):
        with open(self.user_json,'r',encoding='utf8') as f:
            data=json.loads(f.read())
            print("data -type",type(data))
        if time_str ==True:
            for username,v in data.items():
                v['create_time']=timestamp_to_string(v['create_time'])
                v['update_time']=timestamp_to_string(v['update_time'])
                data[username] = v
        return data

    def write_user(self,**user):
        print(user)
        if 'username' not in user:
            raise ValueError('missing username')
        if 'role' not in user:
            raise ValueError('missing role')
        user['active'] =True
        user['create_time'] = time.time()
        user['update_time'] = time.time()
        user['gifts'] = []
        users = self.__read_users()
        print("users",users)
        if user['username'] in users:
            raise myerror.UserExistsError
        users.update(
            {user["username"]:user}
        )
        print("users",users)
        json_users = json.dumps(users)
        with open(self.user_json,'w') as f:
            f.write(json_users)




    def change_role(self,username,role):
        users = self.__read_users() #字典格式
        user = users.get(username)  #"role": "admin", "active": true, "create_time":
        if not user:
            return False
        if role not in ROLES:
            raise myerror.RoleError('not use role {}'.format(role))
        user['role'] = role
        user['update_time'] = time.time()
        users[username] = user
        json_data = json.dumps(users)
        with open(self.user_json,'w') as f:
            f.write(json_data)
        return True

    def change_active(self,username):
        users = self.__read_users() #字典格式
        user = users.get(username)  #"role": "admin", "active": true, "create_time":
        if not user:
            return False
        user['active'] = not user['active']
        user['update_time'] = time.time()
        users[username] = user
        json_data = json.dumps(users)
        with open(self.user_json,'w') as f:
            f.write(json_data)
        return True

    def delete_user(self,username):
        users = self.__read_users() #字典格式
        user = users.get(username)  #"role": "admin", "active": true, "create_time":
        del_user = users.pop(username)
        json_data = json.dumps(users)
        with open(self.user_json,'w') as f:
            f.write(json_data)
        return del_user

if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(),"storage","gift.json")
    user_path = os.path.join(os.getcwd(),"storage","user.json")
    # print(gift_path,user_path)
    base=Base(user_json=user_path,gift_json=gift_path)
    base.write_user(username="daiwei",role="admin")
    # res=base.change_role( username='daiwei',role='normal')
    # res=base.change_active( username='daiwei' )
    # res=base.delete_user(username='daiwei')
    # print(res)