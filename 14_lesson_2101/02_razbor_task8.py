from turtle import *
from random import randint

t = Turtle()
t.pensize(2)
colormode(255)

line = 15  # длина стороны первого квадрата
x = 0  # начальные координаты первого квадрата
y = 0  # начальные координаты первого квадрата

t.speed(0)
for line in range(10000):
    r = randint(10, 255)
    g = randint(10, 255)
    b = randint(10, 255)
    t.color(r, g, b)
    t.fd(line)
    t.rt(90)

    line += 40



done()