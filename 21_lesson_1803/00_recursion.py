from turtle import *


def draw_triangle(turt, length):
    for i in range(3):
        turt.fd(length)
        turt.lt(120)


def pentagon(turt, length):
    for i in range(5):
        turt.fd(length)
        t.rt(72)


def draw_triangle_star(turt, count, angle):
    if count <= 0:
        return None
    else:
        pentagon(turt, 100)
        turt.rt(angle)
        draw_triangle_star(turt, count - 1, angle)

t = Turtle()
t.speed(0)
triangles = 20
draw_triangle_star(t, triangles, 360 / triangles)

done()
