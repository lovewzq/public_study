#标识符号在前面
print("输入格式：")
print("温度：c32/C32")
print("华氏度：f32/F32")
TempStr=input("请输入带符号的温度值：")
#判断输入数据的最后一个字符
if TempStr[0] in ['F','f']:
    C=(eval(TempStr[1:])-32)/1.8
    print("转换后的温度是C{:.2f}".format(C))
elif TempStr[0] in ['C','c']:
    F=(eval(TempStr[1:])*1.8+32)
    print("转换后的温度是F{:.2f}".format(F))
else:
    print("请输入正确的格式！")