def power(num, p):
    """
    Функция возводит одно число в степень другого числа
    :param num: число, которое будут возводить
    :param p: степень, в которую будут возводить
    :return: num ^ p
    """
    res = num ** p
    return res


print(power(2, 7))  # num=2, p=7, res=128
print(power(7, 2))  # num=7, p=2, res=49
# Аргументы передаются в том же порядке, что и параметры функции