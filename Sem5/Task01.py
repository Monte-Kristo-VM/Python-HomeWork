# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(a, b):
    if b == 0:
        return 1
    b -= 1
    return a * exponentiation(a, b)

print(exponentiation(2,10))
