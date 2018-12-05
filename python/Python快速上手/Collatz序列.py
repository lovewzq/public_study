def collatz(number):
    if number==1:
        return number
    if number%2==0:
        tem=number//2
        print(tem)
        return tem
    else:
        tem=number*3+1
        print(tem)
        return tem
try:
    num=int(input("请输入一个整数："))
except:
    print("您输入的内容，不是一个整数！")
while (True):
    temp=collatz(num)
    num=collatz(temp)
    if temp==1:
        break

    

