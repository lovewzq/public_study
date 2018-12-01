import turtle as t 

t.setup(600,600)
t.speed(0)

def Skip(step):
    t.up()
    t.fd(step)
    t.down()

def Skib(x,y):
    t.up()
    t.goto(x,y)
    t.down()

Skib(-144,96)

t.fillcolor("red")
t.color("red")
t.begin_fill()
for i in range(2):
    t.fd(288)
    t.right(90)
    t.fd(192)
    t.right(90)
t.end_fill()


Skib(-124.8,57.6)


t.color("yellow")

def Wu(width):
    for i in range(5):
        t.fd(width)
        t.right(144)
t.fillcolor("yellow")
t.begin_fill()
Wu(57.6)
t.end_fill()

Skib(-57.6,76.8)
t.begin_fill()
Wu(19.2)
t.end_fill()

Skib(-38.4,57.6)
t.begin_fill()
Wu(19.2)
t.end_fill()

Skib(-38.4,28.8)
t.begin_fill()
Wu(19.2)
t.end_fill()

Skib(-57.6,9.6)
t.begin_fill()
Wu(19.2)
t.end_fill()




t.hideturtle()
t.done()