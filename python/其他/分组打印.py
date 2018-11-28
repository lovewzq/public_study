i=1  #行数
j=1  #列数
n=int(input("请输入行数："))
for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")