# -*- coding: UTF-8 -*-
import sys
import importlib
importlib.reload(sys)

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import tkinter as tk


win = tk.Tk()

#图形界面
win.title("邮件发送器")

def mail():
    # 邮件内容
    msg=MIMEText(content,'plain','utf-8')
    # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['From']=formataddr(["xx",'master@mail.homesta.club'])  
    # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['To']=formataddr(["xx",aim])   
    # 邮件的主题           
    msg['Subject']=Subject                
 
    # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
    # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
    # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
    server=smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  
    # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
    server.login('master@mail.homesta.club', 'Zxcvb123456')  
    # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.sendmail('master@mail.homesta.club',[aim,],msg.as_string())  
    # 关闭连接
    server.quit() 
    # 如果 try 中的语句没有执行，则会执行下面的 ret=False 


tk.Label(win, text='邮件发送器').grid(row=0,column=1)

L1 = tk.Label(win, text="目标邮箱").grid(row=1,column=0)
aim=tk.Entry(win,width=12).grid(row=1,column=1)

L2=tk.Label(win,text="邮件主题").grid(row=2,column=0)
Subject=tk.Entry(win,width=12).grid(row=2,column=1)

L2=tk.Label(win,text="邮件内容").grid(row=3,column=0)
content=tk.Entry(win,width=12).grid(row=3,column=1)

bt1=tk.Button(win,text="发送",command=mail).grid(row=4,column=1)


# 进入消息循环
win.mainloop()