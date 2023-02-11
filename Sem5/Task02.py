# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return 0
    if a == 0:
        return 1+sum(a, b-1)
    return 1+sum(a-1, b)


while True:
    number1 = input('Введите первое число: ')
    if number1.isdigit() and number1 != '0':
        number1 = int(number1)
        break
    else:
        print('Некорректный ввод!')

while True:
    number2 = input('Введите второе число: ')
    if number2.isdigit() and number2 != '0':
        number2 = int(number2)
        break
    else:
        print('Некорректный ввод!')

print(f'Сумма чисел {number1} и {number2} = {sum(number1, number2)}')
