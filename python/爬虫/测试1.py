from urllib.request import urlopen
import re
while(True):
    url='http://www.baidu.com'
    html=urlopen(url).read().decode('utf-8')
#得到标题
res = re.findall(r"<title>(.+?)</title>", html)
#得到段落
rep = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)
#得到链接
rea = re.findall(r'href="(.*?)"', html)
print("\nPage paragraph is: ", res[0])
print("\nPage title is: ", rea[0])
