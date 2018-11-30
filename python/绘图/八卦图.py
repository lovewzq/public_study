import turtle as t 

#设置画布大小：600*600
t.setup(600,600)

#设置画笔速度为：0
t.speed(0)

#定义画笔无痕前进函数
def Skip(step):
    t.up()
    t.fd(step)
    t.down()

t.circle(50)
t.up()
t.goto(0,-50)
t.down()

t.circle(100,steps=8) 

t.done()