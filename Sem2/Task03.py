# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
#
# Пример:
# 10 -> 1 2 4 8

while True:
    number = input('Введите число: ')
    if number.isdigit() and number != '0':
        number = int(number)
        break
    else:
        print('Некорректный ввод!')

max_two_exp = 1
i = 0
while max_two_exp <= number:
    print(max_two_exp)
    i += 1
    max_two_exp = 2 ** i

