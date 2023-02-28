# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 16:48
# @Author  : alvin
# @File    : request_qa.py
# @Software: PyCharm
import json

import  requests
res=requests.get(r" https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=110.251.47.36&co=&resource_id=5809&t=1676625301122&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110204161818420442296_1676623151943&_=1676623151961")
# print(res.text)
# res=  res.text
# res = res[res.find('{'):res.rfind('}')+1]
# res = json.loads(res)
# print(res)
a='jQuery110204161818420442296_1676623151943({"Srcid":"5809","ResultCode":"0","status":"0","QueryID":"2476329618","Result":[{"DisplayData":{"strategy":{"tempName":"ip","precharge":"0","ctplOrPhp":"1"},"resultData":{"tplData":{"srcid":"5809","resourceid":"5809","OriginQuery":"110.251.47.36","origipquery":"110.251.47.36","query":"110.251.47.36","origip":"110.251.47.36","location":"\u6cb3\u5317\u7701\u5eca\u574a\u5e02\u5927\u5382 \u8054\u901a","userip":"","showlamp":"1","tplt":"ip","titlecont":"IP\u5730\u5740\u67e5\u8be2","realurl":"http:\/\/www.ip138.com\/","showLikeShare":"1","shareImage":"1","data_source":"AE"},"extData":{"tplt":"ip","resourceid":"5809","OriginQuery":"110.251.47.36"}}},"ResultURL":"http:\/\/www.ip138.com\/","Weight":"2","Sort":"1","SrcID":"5809","ClickNeed":"0","SubResult":[],"SubResNum":"0","ar_passthrough":[],"RecoverCacheTime":"0"}],"data":[{"srcid":"5809","resourceid":"5809","OriginQuery":"110.251.47.36","origipquery":"110.251.47.36","query":"110.251.47.36","origip":"110.251.47.36","location":"\u6cb3\u5317\u7701\u5eca\u574a\u5e02\u5927\u5382 \u8054\u901a","userip":"","showlamp":"1","tplt":"ip","titlecont":"IP\u5730\u5740\u67e5\u8be2","realurl":"http:\/\/www.ip138.com\/","showLikeShare":"1","shareImage":"1"}]'
print(a.rfind('{'))