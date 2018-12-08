#json是一个通用的数据类型,所有的语言都认识;json是一个字符串
import json
info = {"name": "飞飞", "age": "18"}#定义一个字典
f = open('a.json', 'w', encoding='utf-8')#打开文件a.json文件，如果没有文件，就创建，有的话直接写入
res = json.dumps(info, ensure_ascii=False) #把字典转成json串，ensure_ascii=False防止中文乱码的
print(type(res))#打印res的类型是字符串，其实就是json，因为json本身就是字符串
print(res)
f.write(res)#打开a.json后直接写入json串