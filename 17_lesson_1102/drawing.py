def draw_square(obj, x, y, col, line):
    """
    Процедура будет рисовать квадрат по заданным параметрам
    :param obj: черепашка
    :param x: координаты начала рисования
    :param y: координаты начала рисования
    :param color: цвет линии
    :param line: длина стороны
    :return: None
    """
    obj.up()
    obj.goto(x, y)
    obj.color(col)
    obj.down()
    for i in range(4):
        obj.fd(line)
        obj.rt(90)