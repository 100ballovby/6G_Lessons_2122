from turtle import *

t = Turtle()
t.pensize(7)
t.color('#ec24fa')

for branch in range(8):
    for i in range(3):
        for j in range(3):
            t.fd(30)
            t.bk(30)
            t.rt(45)
        t.lt(90)
        t.bk(30)
        t.lt(45)
    t.rt(90)
    t.fd(90)
    t.lt(45)


done()
