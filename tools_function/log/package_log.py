# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 10:42
# @Author  : alvin
# @File    : package_log.py
# @Software: PyCharm
import logging
import os


def init_log(path):
    if os.path.exists(path):
        mode='a.text'
    else:
        mode='w'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
        filename=path,filemode=mode
    )
    return logging

current=os.getcwd()
path = os.path.join(current,'back.log')
log=init_log(path)

log.info("this is first log info")
log.warning("this is first warn log info")