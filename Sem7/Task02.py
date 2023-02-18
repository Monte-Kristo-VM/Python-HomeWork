# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.
#
# Ввод: print_operation_table(lambda x, y: x * y)
# Вывод:
# 1         2         3         4         5          6
# 2         4         6         8         10         12
# 3         6         9         12        15         18
# 4         8        12         16        20         24
# 5        10        15         20        25         30
# 6        12        18         24        30         36

def print_operation_table(operation, num_rows=6, num_columns=6):
    row = [i for i in range(1, num_columns+1)]
    column = [i for i in range(1, num_rows + 1)]
    whitespace=' '
    res_str = ''

    for j in range(1, num_columns+1):
        res_str += str(j) + whitespace * (6 - len(str(j)))
    print(res_str)

    for i in range(2, num_rows+1):
        column = [i for _ in range(num_columns)]
        res = list(map(operation, row, column))
        for j in range(num_columns):
            res[j] = round(res[j],1)
        res_str = str(i)+whitespace*5

        for j in range(1, num_columns):
            res_str += str(res[j]) + whitespace*(6-len(str(res[j])))

        print(res_str)


print_operation_table(lambda x, y: x * y)
print()

print_operation_table(lambda x, y: x / y, 5, 8)
print()

print_operation_table(lambda x, y: x + y, 4, 3)
print()

print_operation_table(lambda x, y: x - y, 3, 5)