from turtle import *


def spiral(obj, size, angle):
    import random as ran
    step = 5
    r = 0
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    for i in range(size):
        obj.color(r, g, b)
        obj.fd(step)
        obj.rt(angle)
        step += 5

        r = (r + 1) % 255

t = Turtle()
colormode(255)  # включить RGB
t.speed(0)
spiral(t, 350, 121)

done()
