def collatz(number):
    if number%2==0:
        tem=number//2
        print(tem)
        return tem
    else:
        tem=number*3+1
        print(tem)
        return tem

num=int(input("请输入一个整数："))
for i in range(10):
    t=collatz(num)
    c=collatz(t)
    

