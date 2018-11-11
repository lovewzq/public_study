#标识符号在后面
print("输入格式：")
print("温度：32c/32C")
print("华氏度：32f/32F")
TempStr=input("请输入带符号的温度值：")
#判断输入数据的最后一个字符
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F=(eval(TempStr[0:-1])*1.8+32)
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("请输入正确的格式！")