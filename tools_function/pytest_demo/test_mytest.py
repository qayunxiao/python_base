# -*- coding: utf-8 -*-
# @Time    : 2023/1/19 16:57
# @Author  : alvin
# @File    : test_pytest2.py
# @Software: PyCharm

import pytest

def add(a,b):
    return  a+b

def test_dengyu():
    assert  3 == add(1,2)

if __name__ == '__main__':
    pytest.main(['test_pytest2.py'])
