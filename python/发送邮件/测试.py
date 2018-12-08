import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart   

import os,sys
from nt import chdir#判断目录是否存在并切换目录

print("脚本运行开始")
#登陆邮件服务器
smtpObj=smtplib.SMTP('smtp.qq.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
#传入相应的账号密码信息
smtpObj.login('2335208932@qq.com', 'jafghkwfamridibd')

#邮件收发信人信息
sender = '2335208932@qq.com'#发件人信息
receivers = ['522990833@qq.com']#收件人信息

#完善发件人收件人，主题信息
message=MIMEMultipart()
message['From'] = formataddr(["发件人昵称",sender]) 
message['To'] = formataddr(["收件人昵称",''.join(receivers)]) 

#邮件标题
subject = '天气预报'
message['Subject'] = Header(subject, 'utf-8')


#正文部分
textmessage = MIMEText('今天天气寒冷，请注意保暖！','plain', 'utf-8')
message.attach(textmessage)


#发送邮件操作
smtpObj.sendmail(sender,receivers, message.as_string())
smtpObj.quit()
print("脚本运行结束")