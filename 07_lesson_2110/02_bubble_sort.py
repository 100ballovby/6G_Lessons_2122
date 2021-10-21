import random as r


array = []  # пустой список

for num in range(5):  # повторить 5 раз
    array.append(r.randint(-100, 100))  # добавить в список случайное число от -100 до 100

print(array)  # вывести список

for iteration in range(len(array) - 1):  # повторить "длина списка" раз
    for element in range(len(array) - iteration - 1):  # так как конец списка УЖЕ отсортирован
        if array[element] > array[element + 1]:  # если текущий элемент больше следующего
            array[element], array[element + 1] = array[element + 1], array[element]
    print(f'Итерация {iteration}: {array}')

print(array)