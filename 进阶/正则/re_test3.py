# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 18:14
# @Author  : alvin
# @File    : re_test3.py
# @Software: PyCharm
import re
def check_url(url):
    re_g = re.compile('[a.text-zA-Z]{4,5}://\w*\.*\w+\.\w+')
    print("check_url",re_g)
    res = re_g.findall(url)
    print("res",res)

def get_email(data):
    #.通配符
    re_g = re.compile('.+@.+\.[a.text-zA-Z]+')
    res =re_g.findall(data)
    print(res)
    return res

if __name__ == '__main__':
    url ='https://www.imocc.com/'
    res = check_url(url)
    print(res)
    email='dewei@imocc.com'
    res2=get_email(email)
    print(res2)
    html=('<div class="s-top-nav" style="display:none;">' '</div><div class="s-center-box"></div>')
    re_g=re.compile('="(.+?)"')
    res3=re_g.search(html)
    print(res3,res3.groups())
    re_g = re.compile('\s')
    res4=re_g.split(html)
    print(res4)
    re_g=re.compile('<div class="(.+?)"')
    res5=re_g.match(html)
    print(res5,res5.span(),html[:22])