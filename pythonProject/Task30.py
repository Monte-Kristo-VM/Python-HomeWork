# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

while True:
    first_element = input('Введите первый элемент последовательности: ')
    if first_element.isdigit():
        first_element = int(first_element)
        break
    else:
        print('Некорректный ввод!')

while True:
    def_element = input('Введите разность арифметической прогрессии: ')
    if def_element.isdigit() and def_element != '0':
        def_element = int(def_element)
        break
    else:
        print('Некорректный ввод!')

while True:
    n_element = input('Введите количество элементов: ')
    if n_element.isdigit() and n_element != '0':
        n_element = int(n_element)
        break
    else:
        print('Некорректный ввод!')

arithmetic_progression = []
for i in range(n_element):
    arithmetic_progression.append(first_element + i*def_element)

print(f'Искомая арифметическая прогрессия: {arithmetic_progression}')
