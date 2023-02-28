# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 14:27
# @Author  : alvin
# @File    : handle_mocktest.py
# @Software: PyCharm
import requests
# 启mock服务 tools_function\mock\moco>Mock_server_run.bat
#java -jar moco-runner-1.1.0-standalone.jar http -p 9999 -c test.json

HOST="http://127.0.0.1:9999"
def get_test_json_mock():
    url = f'{HOST}/sq3'
    payload={"key1":"value1","key2":"value2"}
    #json格式
    resp=requests.post(url,json=payload)
    print(resp.text)

def get_test_forms_mock():
    url = f'{HOST}/sq2'
    payload={"key1":"abc"}
    #forms使用data
    resp=requests.post(url,data=payload)
    print(resp.text)

def get_mock_resp_json():
    url= f'{HOST}/sq4'
    payload={}
    resp=requests.get(url,data=payload)
    print(resp.text)

if __name__ == '__main__':
    get_mock_resp_json()
