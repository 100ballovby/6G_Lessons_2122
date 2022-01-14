from turtle import *  # импортирую черепашку

t = Turtle()  # главный объект (она рисует)
t.shape('turtle')  # устанавливаю форму черепашки

t.color('yellow')

# звездочка
t.begin_fill()  # начать заливку
for i in range(5):
    t.fd(150)
    t.rt(144)
t.end_fill()  # закончить заливку

t.up()
t.goto(100, 200)
t.down()

t.color('orange')  # цвет рисования (цвет линии)
t.fillcolor('yellow')  # цвет заливки
t.pensize(5)
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.lt(72)
    t.fd(100)
    t.rt(144)
    t.stamp()  # оставить отпечаток черепашки
t.end_fill()

done()