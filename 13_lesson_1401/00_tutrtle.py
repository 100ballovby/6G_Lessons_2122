from turtle import *  # импортирую черепашку

t = Turtle()  # главный объект (она рисует)
t.shape('turtle')  # устанавливаю форму черепашки
t.speed(0)  # скорость перемещения (0 - самая высокая)

t.fd(100)  # вперед на 100 шагов
t.lt(45)  # повернуть влево на 45 градусов
t.bk(120)  # назад на 120 шагов
t.rt(90)  # вправо на 90 градусов

for i in range(100):  # повторить 100 раз
    t.rt(50)  # повернуться на 50 градусов

t.pensize(5)  # выбирает толщину линии
colors = ['red', 'orange', 'LightPink', 'DeepSkyBlue2', 'beige']
for c in colors:  # для каждого цвета в списке цветов
    t.color(c)  # заменить цвет черепашки на цвет из списка
    t.fd(50)  # пройти вперед на 50 шагов

done()  # чтобы окно сразу не закрывалось
