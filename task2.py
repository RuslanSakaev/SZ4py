# 2'. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# Например:
# * 6 -> [1,2,3]
# * 144 -> [2,3]

from random import randint as rnd


def dividers(a: int, uniq: bool = False) -> list[int]:
    i = 2
    dividers = []
    while a != 1:
        while a % i == 0:
            dividers.append(i)
            a //= i
        i += 1
    if uniq:
        return list(set(dividers))
    else:
        return dividers


a = rnd(10, 9999)
print(f'Список натуральных делителей числа {a}:{dividers(a)}')
print(f'Список уникальных делителей числа {a}:{dividers(a, True)}')
