# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 17:41
# @Author  : alvin
# @File    : re_test2.py
# @Software: PyCharm
import re

def check_url(url):
    res=re.findall('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+',url)
    if len(res) !=0:
        return True
    return False

def get_email(data):
    #.通配符
    res = re.findall('.+@.+\.[a-zA-Z]+',data)
    print(res)
    return res

def get_url(url):
    res=re.findall('https://(\w*\.*\w+\.\w+)',url)
    if len(res) !=0:
        return res[0]
    return ''

def get_html_style(data):
    res = re.findall('style="(.*?)"',data)
    print(res)
    return res

def get_html_class(data):
    res = re.findall('class="(.*?)"',data)
    return res

if __name__ == '__main__':
    url ='https://www.imocc.com/'
    res = check_url(url)
    res2= get_url(url)
    print(res2)
    email='dewei@imocc.com'
    res3=get_email(email)
    print(res3)
    html=('<div class="s-top-nav" style="display:none;">' '</div><div class="s-center-box"></div>')
    print(html)
    res4=get_html_style(html)
    print(res4)
    res5=get_html_class(html)
    print(res5)