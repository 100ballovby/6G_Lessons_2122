from turtle import *

t = Turtle()

t.circle(50)

t.up()
t.goto(100, 100)
t.down()

t.lt(90)
t.circle(40, 180)  # нарисовать половину круга (180 градусов) с радиусом 40

t.up()
t.goto(-100, -100)
t.down()

t.circle(100, 90)  # Нарисовать четверть круга (90 градусов) с радиусом 100

done()
