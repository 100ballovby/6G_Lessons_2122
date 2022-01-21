from turtle import *

t = Turtle()
t.pensize(5)
colormode(255)  # устанавливаю модель работы с цветом в RGB

x = -50
y = 0

t.up()
t.goto(x, y)
t.down()

t.color(163, 86, 55)  # цвет обводки
t.fillcolor(191, 116, 86)  # цвет заливки

t.begin_fill()
for line in range(4):  # рисую основание дома (стены)
    t.fd(100)
    t.rt(90)
t.end_fill()

x = -70
t.goto(x, y)

t.color(27, 34, 97)
t.fillcolor(65, 75, 166)

t.begin_fill()
for line in range(3):  # рисую крышу
    t.fd(140)
    t.lt(120)
t.end_fill()

x = -40
y = -40
t.up()
t.goto(x, y)
t.down()

t.color(69, 46, 25)
t.fillcolor(125, 88, 55)

t.begin_fill()
for line in range(2):  # рисую дверь
    t.fd(35)
    t.rt(90)
    t.fd(60)
    t.rt(90)
t.end_fill()

x = 5
t.up()
t.goto(x, y)
t.down()

t.color(163, 86, 55)
t.fillcolor(145, 225, 230)

t.begin_fill()
for i in range(4):  # рисую окно
    t.fd(35)
    t.rt(90)
t.end_fill()

done()
