import jieba as jb
t=open('F:\Git\public_study\python\红楼梦探秘\红楼梦3.txt','rb')
content = t.read().decode('utf-8')
cut = jb.cut(content)
print ("-".join(cut))