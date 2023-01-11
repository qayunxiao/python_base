# -*- coding: utf-8 -*-
# @Time    : 2023/1/11 10:28
# @Author  : alvin
# @File    : sendmail.py
# @Software: PyCharm
"""
 pop.qq.com  995
 smtp.qq.com 465
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.qq.com"
mail_user="6449694"
#授权码
mail_pass=""

sender="6449694@qq.com"
receicers=["cracker-lin@qq.com","alvinqa@foxmail.com"]
#内容
message = MIMEText('这是一个测试','plain','utf-8')
message['From']=Header(sender)
#标题
message['Subject']=Header('py测试','utf-8')

print("meassge",message.as_string())
try:
    smtpobj = smtplib.SMTP()
    smtpobj.connect(mail_host,25)
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,receicers,message.as_string())
except smtplib.SMTPException as e:
    print("error:{}".format(e))
