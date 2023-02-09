# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
#
# Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint as RNDi

while True:
    number_of_coins = input('Введите количество монет: ')
    if number_of_coins.isdigit() and number_of_coins != '0':
        number_of_coins=int(number_of_coins)
        break
    else:
        print('Некорректный ввод!')

coins_heads = 0
coins_tails = 0
i = 0

while i < number_of_coins:
    coin = RNDi(0, 1)
    if coin == 1:
        coins_heads +=1
    else:
        coins_tails +=1
    i+=1

print(f'Орлов {coins_heads}, решек {coins_tails}.')

if coins_heads <= coins_tails:
    print(f'Минимально переворачиваем {coins_heads} монет.')
else:
    print(f'Минимально переворачиваем {coins_tails} монет.')