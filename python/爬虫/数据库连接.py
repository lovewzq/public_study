from urllib.request import urlopen
import re
import mysql.connector

url='http://www.baidu.com'
id=3
html=urlopen(url).read().decode('utf-8')
#得到标题
title= re.findall(r"<title>(.+?)</title>", html)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="web_info"
)
mycursor = mydb.cursor()
 
sql = "INSERT INTO web_base (url,title) VALUES (%s,%s)"
val = (url,title)
mycursor.execute(sql, val)
 
mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
print(mycursor.rowcount, "记录插入成功。")