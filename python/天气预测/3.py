while (True):
    A=int(input("请输入等级A的个数："))
    B=int(input("请输入等级B的个数："))
    C=int(input("请输入等级C的个数："))
    D=int(input("请输入等级D的个数："))
    num=int(input("请输入平时成绩："))
    
    sum=A*5+B*4+C*3+D*2+num
    print("该学生的总成绩是：%d"%sum)



