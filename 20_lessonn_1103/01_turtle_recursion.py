from turtle import *


def spiral(turt, length, deg):
    if length <= 0:  # базовый случай
        return None
    else:
        turt.fd(length)
        turt.rt(deg)
        spiral(turt, length - 10, deg)


def zigzag(turt, num, length):
    if num <= 0:
        return None
    else:
        turt.lt(45)
        turt.fd(length)
        turt.rt(90)
        turt.fd(3 * length)
        turt.lt(90)
        turt.fd(length)
        turt.rt(45)
        zigzag(turt, num - 1, length)

t = Turtle()

zigzag(t, 6, 20)
done()
