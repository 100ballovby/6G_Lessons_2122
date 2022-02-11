from turtle import *

t = Turtle()

t.color('red')
for i in range(4):
    t.fd(100)
    t.rt(90)

t.up()
t.goto(100, 100)
t.down()
t.color('green')
for i in range(4):
    t.fd(35)
    t.rt(90)

t.up()
t.goto(-200, 100)
t.down()
t.color('yellow')
for i in range(4):
    t.fd(80)
    t.rt(90)

t.up()
t.goto(200, -200)
t.down()
t.color('blue')
for i in range(4):
    t.fd(120)
    t.rt(90)

t.up()
t.goto(-180, 100)
t.down()
t.color('pink')
for i in range(4):
    t.fd(180)
    t.rt(90)

done()
