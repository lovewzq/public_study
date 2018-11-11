#先选模式，在输出
print("华氏转温度-请输入-H")
print("温度转华氏-请输入-C")
modo=input("请选择转换模式：")
Tem=int(input("请输入温度："))

if modo=='H':
    C=(Tem-32)/1.8
    print("%d华氏度=%d温度"%(Tem,C))
elif modo=='C':
    F=Tem*1.8+32
    print("%d温度=%d华氏度"%(Tem,F))
else:
    print("选择模式错误！！")


