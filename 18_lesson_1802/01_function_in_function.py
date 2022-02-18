from turtle import *


def filled_square(obj, col, line):
    obj.color(col)
    obj.fillcolor(col)
    obj.begin_fill()
    for i in range(4):
        obj.fd(line)
        obj.rt(90)
    obj.end_fill()


def lined_square(obj, col, line):
    obj.color(col)
    for i in range(4):
        obj.fd(line)
        obj.rt(90)


def draw_square(obj, x, y, col, line, filled):
    obj.up()
    obj.goto(x, y)
    obj.color(col)
    obj.down()

    if filled:  # filled == True
        filled_square(obj, col, line)
    else:
        lined_square(obj, col, line)

t = Turtle()

draw_square(t, 100, 100, 'cyan', 100, True)
draw_square(t, -100, -100, 'red', 100, False)

done()
