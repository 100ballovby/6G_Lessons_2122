"""Нужно написать программу, которая
посчитает сумму всех чисел от 1 до 50"""
summary = 0     # в ней считаю сумму чисел

for number in range(1, 51):  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    summary += number

print(f'Сумма всех чисел от 1 до 50: {summary}.')


