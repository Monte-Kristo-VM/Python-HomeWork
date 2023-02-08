number = int(input('Введите трехзначное число: '))
if 99 < number < 1000:
    print(f'Сумма цифр введенного числа = {number%10+number//10%10+number//100%10}')
else:
    print('Вы ввели не трехзначное число!')
