from turtle import *


t = Turtle()
t.speed(0)
red = 0
green = 100
blue = 160
i = 0  # отвечает за количество повторений цикла
while i <= 255:
    colormode(255)
    t.color(red, green, blue)
    t.fd(50 + i)  # длина стороны квадрата будет расти с количеством повторений цикла
    t.rt(91.5)

    i += 1
    red += 1

done()
