number_a = float(input('Введите число 1: '))
number_b = float(input('Введите число 2: '))
'''чтобы сдублировать строчку, нажмите ctrl+d'''

print(f'{number_a} + {number_b} = {number_a + number_b}')
# форматированная строка - можно вставить значение переменной в строку
print(f'{number_a} - {number_b} = {number_a - number_b}')
print(f'{number_a} * {number_b} = {number_a * number_b}')
print(f'{number_a} // {number_b} = {number_a // number_b}')
print(f'{number_a} ** {number_b} = {number_a ** number_b}')

name = input('Как тебя зовут? ')
print(f'Привет, {name}!')