from turtle import *
from random import randint, choice
from drawing import draw_square  # из [название_файла] импортировать [название_функции]

colors = ['#32a852', '#63826b', '#5d16c7', '#c7165d',
          '#f5ff40', '#7cff40', '#ff8c40', '#df40ff']

t = Turtle()
t.speed(0)
t.pensize(4)

for i in range(555):
    x = randint(-400, 400)
    y = randint(-400, 400)
    length = randint(40, 200)
    color = choice(colors)
    draw_square(t, x, y, color, length)

done()
