f= open("F:\Git\public_study\python\自动邮件天气预报\weather.txt", "r",encoding='utf-8')
text=f.read()
print(text)
# 关闭打开的文件
f.close()