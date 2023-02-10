# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9
import random

while True:
    number = input('Введите число кустов: ')
    if number.isdigit() and number != '0' and number != '1' and number != '2':
        number = int(number)
        break
    else:
        print('Некорректный ввод!')

blueberries = [random.randint(1, 20) for _ in range(number)]
print(blueberries)

max_blu = 0
for i in range(len(blueberries)):
    if i < len(blueberries)-2:
        if max_blu<blueberries[i]+blueberries[i+1]+blueberries[i+2]:
            max_blu=blueberries[i]+blueberries[i+1]+blueberries[i+2]
    else:
        if max_blu<blueberries[i]+blueberries[i-len(blueberries)+1]+blueberries[i-len(blueberries)+2]:
            max_blu=blueberries[i]+blueberries[i-len(blueberries)+1]+blueberries[i-len(blueberries)+2]
print(f'Максимальное число ягод = {max_blu}')