from turtle import *


def square(turt, length):
    for i in range(4):
        turt.fd(length)
        turt.rt(90)


def nautilus(turt, angle, length):
    if length >= 200:
        return None
    else:
        square(turt, length)
        t.lt(angle)
        nautilus(turt, angle, length + 5)

t = Turtle()
t.speed(0)
nautilus(t, 10, 5)

done()