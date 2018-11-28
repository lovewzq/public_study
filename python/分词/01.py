import jieba as jb
t=open('F:\Git\public_study\python\分词\测试1.txt','rb')
content = t.read().decode('utf-8')
cut = jb.cut(content)
print ("-".join(cut))