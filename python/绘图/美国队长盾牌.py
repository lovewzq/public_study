import turtle as t 

t.setup(600,600)

def Skip(step):
    t.up()
    t.fd(step)
    t.down()

#t.mode("logo")
t.fillcolor('red')
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()

t.goto(0,20)

t.fillcolor('white')
t.color('white')
t.begin_fill()
t.circle(80)
t.end_fill()

t.goto(0,40)

t.fillcolor('red')
t.color('red')
t.begin_fill()
t.circle(60)
t.end_fill()

t.goto(0,60)

t.fillcolor('blue')
t.color('blue')
t.begin_fill()
t.circle(40)
t.end_fill()

t.goto(-40,110)

t.fillcolor('white')
t.color('white')
t.begin_fill()
for i in range(5):
    t.fd(80)
    t.rt(144)
t.end_fill()

t.hideturtle()

t.done()