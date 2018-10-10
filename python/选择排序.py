list=[10,3,4,2,4,33,43,25,4,32,52,5,42,89,5,5,47,65,7]
length=len(list)
while length>0:
    for i in range(0,length-1):
        minindex=i
        for j in range(1,length):
            if list[j]<list[i]:  #找到列表中最小的元素
                minindex=j
        temp=list[i]
        list[i]=list[minindex]
        list[minindex]=temp
    length=length-1
print(list)
