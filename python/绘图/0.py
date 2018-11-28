import turtle as t 

t.setup(600,600)
t.speed(0)

#t.mode("stantard")

def Skip(step):
    t.up()
    t.fd(step)
    t.down()

t.fillcolor('black')
t.color('black')
t.begin_fill()
t.circle(100,180)
t.end_fill()


t.color('black')
t.fillcolor('white')
t.begin_fill()
t.circle(100,180)
t.end_fill()

t.goto(0,0)

t.color('black')
t.fillcolor('white')
t.begin_fill()
t.circle(50,180)
t.end_fill()

t.goto(0,100)

t.color('black')
t.fillcolor('black')
t.begin_fill()
t.circle(-50,180)
t.end_fill()

t.up()
t.goto(0,75)
t.down()

t.color('black')
t.fillcolor('black')
t.begin_fill()
t.circle(-20)
t.end_fill()

t.up()
t.goto(0,175)
t.down()

t.color('black')
t.fillcolor('white')
t.begin_fill()
t.circle(-20)
t.end_fill()

t.hideturtle()

t.done()