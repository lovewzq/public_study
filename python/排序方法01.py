list=[41,52,13,14,51,42,49,85,23,16]
length=len(list)
while length>0:
    i=0
    while i<length-1:
        if list[i]>list[length-1]:
            temp=list[length-1]
            list[length-1]=list[i]
            list[i]=temp
            length=len(list)
        i=i+1
    length=length-1
print(list)