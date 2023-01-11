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
from email.mime.multipart import MIMEMultipart
 
mail_host="smtp.qq.com"
mail_user="6449694"
#授权码
mail_pass="yhqtwpohmdvecada"

sender="6449694@qq.com"
receicers=["cracker-lin@qq.com","alvinqa@foxmail.com"]
#内容
message = MIMEMultipart()
#hmtl 文字红色
message['From']=Header(sender)
#标题
message['Subject']=Header('py测试','utf-8')
#组装附件内容
attr=MIMEText(open('sendmail.py','rb').read(),'base64','utf-8')
attr["Content-Type"]="application/octet-stream"
attr["Content-Disposition"]='attachment;filename="sendmail.py"'
message.attach(attr)

#标题
message.attach(MIMEText('这是一个带附件的邮件','plain','utf-8'))
try:
    smtpobj = smtplib.SMTP()
    smtpobj.connect(mail_host,25)
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,receicers,message.as_string())
except smtplib.SMTPException as e:
    print("error:{}".format(e))
