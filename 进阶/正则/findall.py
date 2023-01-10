# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 16:54
# @Author  : alvin
# @File    : findall.py
# @Software: PyCharm
import  re
def had_number(data):
    # [0-9]任意一个
    res = re.findall('\d',data)
    # if len(res) !=0 :
    #     return True
    # else:
    #     return False
    for i in res:
        return True
    return False

def remove_number(data):
    # 非字母字符返回列表
    res =re.findall("\D",data)
    print(res)
    #列表返回字符串
    return ''.join(res)

def startwith(sub,data):
    _sub = '\A{}'.format(sub)
    res = re.findall(_sub,data)
    for i in res:
        return True
    return False

def endswith(sub,data):
    _sub = '{}\Z'.format(sub)
    print(_sub)
    res = re.findall(_sub,data)
    print(res)
    for i in res:
        return True
    return False

def real_len(data):
    res = re.findall('\S',data)
    return len(res)


if __name__ == '__main__':
    data = "i am dewei ,i am "
    res=had_number(data)
    print(res)
    res2=remove_number(data)
    print("remove_number",res2)

    data = "hello xiaomu.i am dewei ,i am 33 year old"
    print(re.findall('\W',data))

    res3=startwith('hell',data)
    print(res3)

    res4=endswith('olds',data)
    print(res4)

    print(len(data))
    res5=real_len(data)
    print(res5)