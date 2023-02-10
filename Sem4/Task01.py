# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. Пользователь вводит 2 числа.
# n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# Размер первого списка
while True:
    length1 = input('Введите количество элементов первого множества: ')
    if length1.isdigit() and length1 != '0':
        length1 = int(length1)
        break
    else:
        print('Некорректный ввод! Введите целое число!')

# Размер второго списка
while True:
    length2 = input('Введите количество элементов второго множества: ')
    if length2.isdigit() and length2 != '0':
        length2 = int(length2)
        break
    else:
        print('Некорректный ввод! Введите целое число!')

# Ввод значений первого списка
list1 = []
i = 0
while i < length1:
    while True:
        number = input(f'Введите {i + 1} элемент первого списка: ')
        if number.isdigit() and number != '0':
            list1.append(int(number))
            i += 1
            break
        else:
            print('Некорректный ввод! Введите целое число!')

print('Следующий список, погнали ->')

# Ввод значений второго списка
list2 = []
i = 0
while i < length2:
    while True:
        number = input(f'Введите {i + 1} элемент второго списка: ')
        if number.isdigit() and number != '0':
            list2.append(int(number))
            i += 1
            break
        else:
            print('Некорректный ввод! Введите целое число!')

print(f'Первый список из {length1} элементов:')
print(list1)
print(f'Второй список из {length2} элементов:')
print(list2)

# Пресечение двух множеств
list_cross = set(list1).intersection(set(list2))

if len(list_cross) > 0:
    # Преобразуем множество в список, сортируем и выводим на печать
    list_cross = list(list_cross)
    list_cross.sort()
    print('Числа, встречающиеся в обоих наборах (в порядке возрастания):')
    print(*list_cross)
else:
    print('Одинаковых чисел нет!')
