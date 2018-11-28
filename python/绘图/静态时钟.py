# coding=utf-8

import turtle as t

#设置画布
t.setup(800,800)
#设置画笔速度
t.speed(0)
#隐藏画笔箭头
#t.hideturtle()
#设置画笔抬起，画笔前进，画笔落下
def Skip(step,x=0,y=0):
    t.up()
    t.goto(x,y)
    t.fd(step)
    t.down()

t.up()
t.goto(0,-100)
t.down()
t.pensize(5)
#t.circle(200)
t.left(90)
for i in range(12):
    t.pensize(10)
    t.up()
    t.goto(0,100)
    t.down()
    t.right(30)
    t.up()
    t.fd(180)
    t.down()
    t.fd(20)

for i in range(60):
    t.pensize(2)
    t.up()
    t.goto(0,100)
    t.down()
    t.right(6)
    t.up()
    t.fd(190)
    t.down()
    t.fd(10)
#时针
t.up()
t.goto(0,100)
t.down()
t.right(90)
t.pensize(8)
t.fd(60)

#分钟
t.up()
t.goto(0,100)
t.down()
t.pensize(5)
t.left(90)
t.fd(110)
#秒针
t.up()
t.goto(0,100)
t.down()
t.pensize(2)
t.right(45)
t.fd(145)



#数字1
t.left(45)

Skip(210,0,100)
t.write(12,align="center",font =("Arial",18,"normal"))
t.right(94)

Skip(220,0,100)
t.write(3,align="center",font =("Arial",18,"normal"))
t.right(86)

Skip(240,0,100)
t.write(6,align="center",font =("Arial",18,"normal"))
t.right(86)

Skip(220,0,100)
t.write(9,align="center",font =("Arial",18,"normal"))

t.hideturtle()





t.done()
