from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url='https://movie.douban.com/subject/27605698/?tag=%E7%83%AD%E9%97%A8&from=gaia_video'
html=urlopen(url).read().decode('utf-8')

soup=BeautifulSoup(html,features='lxml')

#导演与上映年份
t1=soup.find_all('h1')
