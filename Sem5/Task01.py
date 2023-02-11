# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(a, b):
    if b == 0:
        return 1
    b -= 1
    return a * exponentiation(a, b)


while True:
    number = input('Введите число, которое нужно возвести в степень: ')
    if number.isdigit() and number != '0':
        number = int(number)
        break
    else:
        print('Некорректный ввод!')

while True:
    exp = input('Введите степень числа: ')
    if exp.isdigit() and exp != '0':
        exp = int(exp)
        break
    else:
        print('Некорректный ввод!')

print(f'Число {number} в степени {exp} = {exponentiation(number, exp)}')