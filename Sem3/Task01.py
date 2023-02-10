# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

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
    list_rnd.append(randint(1, 100))
print(list_rnd)

while True:
    number = input('Введите искомое число: ')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('Некорректный ввод! Введите натуральное число!')

if number in list_rnd:
    count_number = list_rnd.count(number)
    print(f'Число {number} встречается {count_number} раз(а)')
else:
    near_number = 0
    diff = 100
    for i in list_rnd:
        if abs(i-number) < diff:
            diff = abs(i-number)
            near_number = i
    print(f'Число {number} не содержится в заданном списке.')
    print(f'Ближайшее число {near_number}.')

