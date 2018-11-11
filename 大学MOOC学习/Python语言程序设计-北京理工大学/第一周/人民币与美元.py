T=input("请输入带符号的货币值：")
#判断输入数据的最后一个字符
if T[0] in ['u','U']:
    if T[1] in ['s','S']:
        if T[2] in ['d','D']:
            C=(eval(T[3:]))*6.78
            print("RMB{:.2f}".format(C))
elif T[0] in ['r','R']:
    if T[1] in ['m','M']:
        if T[2] in ['b','B']:
            C=(eval(T[3:]))/6.78
            print("USD{:.2f}".format(C))