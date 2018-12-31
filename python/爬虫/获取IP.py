from bs4 import BeautifulSoup
import time
import requests
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='python')
cur = conn.cursor()

#请求头
headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
}

page=1
IPurl = 'http://www.xicidaili.com/nn/%s' %page
rIP=requests.get(IPurl,headers=headers)

#获取全部页面内容
IPContent=rIP.text

#去除多余内容，空行
sourIP = BeautifulSoup(IPContent,'lxml')

id=int(time.time())

f = open("E:\\ip.txt","a")

#获取表格内容
trs = sourIP.find_all('tr')
for tr in trs[1:]:
    tds = tr.find_all('td')
    #获取ip地址
    ip = tds[1].text.strip()
    #获取端口
    port = tds[2].text.strip()
    #获取协议
    protocol = tds[5].text.strip()
    f.write(ip+':'+port+'\n')
f.close()

