# 3'. Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from random import randint as rnd

mass = [rnd(1, 7) for i in range(12)]
print(f'Исходный список: {mass}')
print(f'Список уникальных элементов: {list(set(mass))}')
mass = [i for i in mass if mass.count(i) == 1]

print(f'Uniq: {mass}')
