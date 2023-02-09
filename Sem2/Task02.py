# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
#
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3*


# ТЕОРИЯ

# Пусть х1 и х2 искомые числа, тогда
# у1=х1+х2
# у2=х1*х2
# Из первого уравнения х2=y1-x1
# Подставляем во второе, получаем
# у2=х1*(у1-х1)
# Открываем скобки, получаем квадратное уравнение
# у2=х1*у1-х1*х1
# х1*х1-у1*х1+y2=0
# Далее нужно решить квадратное уравнение.
# Дискриминанат D=y1*y1-4*y2
# Если дискриминант <0, то уравнение не имеет решения,
# если D=0, то уравнение имеет один корень,
# если D>0, то уравнение имеет два корня
# Корни уравнения
#     х1_1=(у1+sqrt(D))/2
#     х1_2=(у1-sqrt(D))/2
# Далее находим значения х2 по формуле выше
# УДАЧИ НАМ!

from math import sqrt

# Ввод суммы чисел
while True:
    sum_of_numbers = input('Введите сумму загадочных чисел: ')
    if sum_of_numbers.isdigit():
        sum_of_numbers = int(sum_of_numbers)
        break
    else:
        print('Некорректный ввод!')

# Ввод произведения чисел
while True:
    multi_of_numbers = input('Введите произведение загадочных чисел: ')
    if multi_of_numbers.isdigit():
        multi_of_numbers = int(multi_of_numbers)
        break
    else:
        print('Некорректный ввод!')

# Нахождение дискриминанта уравнения D
D = sum_of_numbers ** 2 - 4 * multi_of_numbers

# Проверка возможности решения уравнения:

# Один корень
if D == 0:
    x1 = int(sum_of_numbers / 2)
    x2 = int(sum_of_numbers - x1)
    if 0 < x1 <= 1000 and 0 < x2 <= 1000:
        print(f'Первое загаданное число = {x1}')
        print(f'Второе загаданное число = {x2}')
    else:
        print('У нас проблемка, числа должны быть не больше 1000...')

    # Два корня
elif D > 0:
    x1_1 = (sum_of_numbers + sqrt(D)) / 2
    x2_1 = sum_of_numbers - x1_1
    x1_2 = (sum_of_numbers - sqrt(D)) / 2
    x2_2 = sum_of_numbers - x1_2
    if (0 < x1_1 <= 1000 and 0 < x2_1 <= 1000) or (0 < x1_2 <= 1000 and 0 < x2_2 <= 1000):
        if x1_1 - int(x1_1) == 0:
            print(f'Первое загаданное число = {int(x1_1)}')
            print(f'Второе загаданное число = {int(x2_1)}')
        if x1_2 - int(x1_2) == 0 and x1_1 != x2_2:
            print(f'Первое загаданное число = {int(x1_2)}')
            print(f'Второе загаданное число = {int(x2_2)}')
        if x1_1 - int(x1_1) != 0 and x1_2 - int(x1_2) != 0:
            print('Ну и где Ты взял такие числа?!!')
    else:
        print('У нас проблемка, числа должны быть не больше 1000...')

    # Корни отсутствуют
else:
    print('Такие числа бывают только в сказке!!!')

#  ЗАДАЧА СУПЕР!!! :)
