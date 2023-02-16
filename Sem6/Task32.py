# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

while True:
    length = input('Задайте длину списка: ')
    if length.isdigit() and length != '0':
        length = int(length)
        break
    else:
        print('Некорректный ввод! Введите натуральное число!')

list_rnd = []

for _ in range(length):
    list_rnd.append(randint(1, 20))
print(list_rnd)

while True:
    number_min = input('Задайте минимальное значение: ')
    if number_min.isdigit() and number_min != '0':
        number_min = int(number_min)
        break
    else:
        print('Некорректный ввод! Введите натуральное число!')

while True:
    number_max = input('Задайте максимальное значение: ')
    if number_max.isdigit() and number_max != '0':
        number_max = int(number_max)
        break
    else:
        print('Некорректный ввод! Введите натуральное число!')

index_min_max = []

for i in range(length):
    if number_min <= list_rnd[i] <= number_max:
        index_min_max.append(i)
print(f'Индексы элементов списка в диапазоне от {number_min} до {number_max} включительно равны:')
print(index_min_max)