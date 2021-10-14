"""Я хочу наполнить список случайными числами, которые делятся на 3"""
import random as r

my_list = []

# for i in range(10):
while len(my_list) < 10:  # теперь цикл будет наполнять список числами, пока чисел не будет 10
    # len(x) <- измеряет длину элемента x
    rand_num = r.randint(1, 100)

    if rand_num % 3 == 0:
        my_list.append(rand_num)
print(my_list)
