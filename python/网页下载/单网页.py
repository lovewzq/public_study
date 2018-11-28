from urllib.request import urlopen
import re
#目标网页
url='http://www.baidu.com'
html=urlopen(url).read().decode('utf-8')

f= open("e:\\20181118.html", "w",encoding='utf-8')
f.write(html)

# 关闭打开的文件
f.close()