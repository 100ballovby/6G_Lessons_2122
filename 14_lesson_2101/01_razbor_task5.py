from turtle import *

t = Turtle()
t.pensize(5)
colormode(255)

line = 15  # длина стороны первого квадрата
x = 0  # начальные координаты первого квадрата
y = 0  # начальные координаты первого квадрата

# устанавливаю начальный цвет
r = 100
g = 56
b = 99

for square in range(20):
    t.color(r, g, b)

    for l in range(4):
        t.fd(line)
        t.rt(90)

    t.up()
    x -= 10
    y += 10
    t.goto(x, y)
    t.down()

    r += 3
    g += 7
    b += 8

    line += 20



done()
