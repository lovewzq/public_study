import turtle as t 

t.setup(600,600)

def Skip(step):
    t.up()
    t.fd(step)
    t.down()

#五角星
def Wu(width):
    for i in range(5):
        t.fd(width)
        #Skip(20)
        t.fd(width)
        t.right(144)
Skip(-200)
Wu(200)
t.done()