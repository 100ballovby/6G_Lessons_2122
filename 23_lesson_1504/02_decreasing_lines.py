from turtle import *


def spiral(obj, length):
    while length > 0:
        obj.fd(length)
        obj.bk(length)

        obj.up()
        obj.rt(90)
        t.fd(10)
        obj.lt(90)
        obj.down()
        length -= 5

t = Turtle()
t.speed(0)

spiral(t, 90)

done()
