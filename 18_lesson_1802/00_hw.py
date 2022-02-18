from turtle import *


def draw_triangle(obj, x, y, col, line):
    obj.up()
    obj.goto(x, y)
    obj.color(col)
    obj.down()

    for i in range(3):
        obj.fd(line)
        obj.lt(120)


def draw_rectangle(obj, x, y, col, line):
    obj.up()
    obj.goto(x, y)
    obj.color(col)
    obj.down()
    for i in range(2):
        obj.fd(line * 2)  # длинная сторона прямоугольника
        obj.rt(90)
        obj.fd(line)  # коротка сторона прямоугольника
        obj.rt(90)

t = Turtle()

draw_triangle(t, 100, 100, 'red', 100)
draw_rectangle(t, -100, -100, 'blue', 100)

done()
