# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 13:51
# @Author  : alvin
# @File    : json.py
# @Software: PyCharm
import  json

# with open("json1.json",encoding='utf-8') as f :
#     res = json.load(f)
#     # print(res,type(res))
#     print(res.get("name"))
#     print(res.get('address').get('city'))

my_list=[("admin","password成功"),("alvin","123456")]
with open("jsonw.json",'w',encoding="utf-8") as fw:
    json.dump(my_list,fw,ensure_ascii=False,indent=2)#ensure_ascii不已ASCII方式显示,indent缩进
