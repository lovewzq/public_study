#引入模块
import re
from urllib.request import urlopen

html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')
#查找链接
res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)
#print(html)