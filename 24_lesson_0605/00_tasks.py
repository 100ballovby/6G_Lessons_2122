"""Напишите функцию, которая получает в качестве аргумента
строчку и выводит ее, преобразовывая все буквы в верхний регистр
(делает все буквы большими)."""


def upper_case(string):
    print(string.upper())


upper_case('привет')

"""Напишите функцию, которая получает в качестве аргумента строчку 
и выводит ее, преобразовывая все буквы в нижний регистр."""


def lower_case(string):
    print(string.lower())


lower_case('ПРИВЕТ')

"""Напишите функцию, которая получает строчку через аргумент 
и возвращает количество символов в этой строке."""


def count_symbols(string):
    return len(string)


print(count_symbols('привет, как ты?'))

"""Напишите функцию, которая получает строчку и символ через 
аргументы и проверяет, есть ли заданный символ в строке."""


def check_symbol(string, symbol):
    return symbol in string


print(check_symbol('семья', 'я'))

"""* Напишите функцию, которая получает строчку через аргумент 
и возвращает количество символов в этой строке БЕЗ ПРОБЕЛОВ"""


def without_spaces(string):
    symbols = 0
    for symbol in string:
        if symbol != ' ':
            symbols += 1
    return symbols


print(without_spaces('Привет, как ты?'))