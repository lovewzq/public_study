goal=25
i=0
n=100
print ("请输入[1-100]的一个数字：")
while i<n:
	number=int(input(""))
	
	if number<goal:
		print("小了！")
		continue
	elif number>goal:
		print("大了！")
		continue
	else:
		print("恭喜你猜对了,这个数字是：",number)
		break
	i=i+1

