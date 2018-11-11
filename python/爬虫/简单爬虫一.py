from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("https://music.163.com/#/playlist?id=2331136477").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])