from turtle import *  # импортирую черепашку
from random import randint, choice

t = Turtle()  # главный объект (она рисует)
t.shape('turtle')  # устанавливаю форму черепашки

colors = ['yellow', 'orange', 'purple', 'DeepSkyBlue',
          'coral', 'gold', 'hotpink', 'SlateBlue1']
t.up()

for i in range(100):
    t.color(choice(colors))  # беру случайный цвет линии
    t.fillcolor(choice(colors))  # беру случайный цвет заливки
    x = randint(-500, 500)
    y = randint(-500, 500)
    t.goto(x, y)
    t.dot(randint(5, 100))


done()
