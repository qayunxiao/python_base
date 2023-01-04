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
from common.consts import ROLES,FIRSTLEVELS,SECONDLEVELS
class Base(object):
    def __init__(self,user_json,gift_json):
        self.user_json= user_json
        self.gift_json= gift_json
        self.__check_user_json()
        self.__check_gift_json()
        self.__init_gifts()

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
        self.__save(users, self.gift_json)





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
        self.__save(users, self.gift_json)
        return True

    def change_active(self,username):
        users = self.__read_users() #字典格式
        user = users.get(username)  #"role": "admin", "active": true, "create_time":
        if not user:
            return False
        user['active'] = not user['active']
        user['update_time'] = time.time()
        users[username] = user
        self.__save(users, self.gift_json)
        return True

    def delete_user(self,username):
        users = self.__read_users() #字典格式
        user = users.get(username)  #"role": "admin", "active": true, "create_time":
        del_user = users.pop(username)
        self.__save(users, self.gift_json)
        return del_user

    #读取gift_json
    def __read_gifts(self):
        with open(self.gift_json) as f:
            json_data=json.loads(f.read())
        return json_data

    def __init_gifts(self):
        print("__init_gifts")
        data={
            'level1':{
                'level1':{},
                'level2':{},
                'level3':{}
            },
            'level2':{
                'level1':{},
                'level2':{},
                'level3':{}
            },
            'level3':{
                'level1':{},
                'level2':{},
                'level3':{}
            },
        }
        gifts= self.__read_gifts()
        print("gifts",gifts,len(gifts))
        if len(gifts) != 0:
            return
        self.__save(data, self.gift_json)

    def write_gift(self,first_level,second_level,gift_name,gift_count):
        #判断是否合法
        if first_level not in FIRSTLEVELS:
            raise myerror.LevelError('firstlevel not exists')
        if second_level not in SECONDLEVELS:
            raise myerror.LevelError('secondlevel not exists')

        gifts = self.__read_gifts()

        current_gift_pool = gifts[first_level]
        current_second_gift_pool = current_gift_pool[second_level]

        if gift_count <= 0:
            gift_count = 1

        if gift_name in current_second_gift_pool:
            current_second_gift_pool[gift_name]['count'] = current_second_gift_pool[gift_name]['count'] + gift_count
        else:
            current_second_gift_pool[gift_name] = {
                'name': gift_name,
                'count': gift_count
            }
        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool
        self.__save(gifts, self.gift_json)

        gifts = self.__read_gifts()
        print(gifts)

    def gift_update(self,first_level,second_level,gift_name,gift_count=1):
        #判断是否合法
        if first_level not in FIRSTLEVELS:
            raise myerror.LevelError('firstlevel not exists')
        if second_level not in SECONDLEVELS:
            raise myerror.LevelError('secondlevel not exists')
        #读取gifts字典
        gifts = self.__read_gifts()
        current_gift_pool = gifts[first_level]
        current_second_gift_pool = current_gift_pool[second_level]
        if gift_name not in current_second_gift_pool:
            return False
        current_gift = current_second_gift_pool[gift_name]


        print("gift_count",gift_count)
        print("current_gift['count']",current_gift['count'])
        if  current_gift['count'] - gift_count  < 0:
            raise myerror.NegativeNumberError("gift count can not nagative")
        current_gift['count'] -= gift_count
        current_second_gift_pool[gift_name] =current_gift
        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool
        self.__save(gifts,self.gift_json)

    def delete_gift(self,first_level,second_level,gift_name):
        #判断是否合法
        if first_level not in FIRSTLEVELS:
            raise myerror.LevelError('firstlevel not exists')
        if second_level not in SECONDLEVELS:
            raise myerror.LevelError('secondlevel not exists')
        #读取gifts字典
        gifts = self.__read_gifts()
        current_gift_pool = gifts[first_level]
        current_second_gift_pool = current_gift_pool[second_level]
        delete_gift_data = current_second_gift_pool.pop(gift_name)
        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool
        self.__save(gifts, self.gift_json)
        return delete_gift_data

    def __save(self,data,path):
        json_data = json.dumps(data)
        with open(path,'w') as f:
            f.write(json_data)

if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(),"storage","gift.json")
    user_path = os.path.join(os.getcwd(),"storage","user.json")
    # print(gift_path,user_path)
    base=Base(user_json=user_path,gift_json=gift_path)
    # base.write_user(username="daiwei",role="admin")
    # res=base.change_role( username='daiwei',role='normal')
    # res=base.change_active( username='daiwei' )
    # res=base.delete_user(username='daiwei')
    base.gift_update(first_level='level1',second_level='level2',gift_name='xinhua2',gift_count=1)

