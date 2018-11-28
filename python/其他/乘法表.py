i = 1
# 使用while循环n次，列出行数
while i<=9:
    j = 1    #每行都需要从第一列开始
    # 小循环处理列数
    while j <= i:
        print("%d*%d=%d" % (i,j,i*j), end=",")
        j += 1
    print("")
    i += 1