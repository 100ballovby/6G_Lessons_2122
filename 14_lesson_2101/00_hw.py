from turtle import *

t = Turtle()
t.shape('turtle')
t.pensize(5)
x = -50
y = 0

t.up()
t.goto(x, y)
t.down()

t.color('#96491a')  # цвет линии
t.fillcolor('#cc8356')  # цвет заливки

t.begin_fill()
for i in range(4):
    t.fd(100)
    t.rt(90)
t.end_fill()

x = -70
t.up()
t.goto(x, y)
t.down()

t.color('#8c271d')
t.fillcolor('#c9392c')

for i in range(3):
    t.fd(140)
    t.lt(120)

x = -40
y = -45
t.up()
t.goto(x, y)
t.down()

for i in range(2):
    t.fd(30)
    t.rt(90)
    t.fd(55)
    t.rt(90)

x = 10
t.up()
t.goto(x, y)
t.down()

for i in range(4):
    t.fd(30)
    t.rt(90)


done()
