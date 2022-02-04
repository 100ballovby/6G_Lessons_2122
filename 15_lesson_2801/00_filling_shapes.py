from turtle import *

t = Turtle()
t.pencolor('#69d8e0')  # цвет обводки
t.fillcolor('#6cb048')  # цвет заливки
t.pensize(6)  # толщина линии

t.begin_fill()  # начать заливку
for i in range(4):  # нарисовать квадрат
    t.fd(100)
    t.rt(90)
t.end_fill()  # закончить заливку

done()
