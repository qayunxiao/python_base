# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 20:23
# @Author  : alvin
# @File    : case4聊天机器人.py
# @Software: PyCharm
rebot = "AI"
while True:
    user_mess = input("我:")
    if "名字" in user_mess:
        print("{}:我的名字叫{}".format(rebot,rebot))
    elif user_mess.find("学习") > -1:
        print("{} ：我跟alvin学习的".format(rebot))
    elif "老师" in user_mess:
        print("{}：我真鄙视你，你连lavin老师都不知道".format(rebot))
    elif "水果" in user_mess:
        print("{}：喜欢的水果很多，比如香蕉，苹果".format(rebot))
    elif "再见" in user_mess:
        print("{}: 再见了".format(rebot))
        break
    else:
        print("{}去休息了 充电".format(rebot))
        break