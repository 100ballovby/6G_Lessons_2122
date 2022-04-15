from turtle import *


def spiral(obj, angle, length):
    while length > 0:
        obj.fd(length)
        obj.lt(angle)
        length -= 5

t = Turtle()
t.speed(0)

spiral(t, 90, 320)

done()
