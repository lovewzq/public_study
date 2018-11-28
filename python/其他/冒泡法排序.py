list=[1,2,3,4,5,6,1,2,4,5,3,6]
length=len(list)
while length>0:
    for i in range(0,length):
        for j in range(0,length):
            if list[i]<list[j]:
                num=list[i]
                list[i]=list[j]
                list[j]=num
    length=length-1
print(list)
