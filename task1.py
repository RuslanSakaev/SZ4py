# 1'. Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

# k = 1
# π = 0
# for k in range(1, 1000000):
#     π = π+4*((-1)**(k+1))/(2*k-1)
# print(round(π, 4))

from math import pi


def format_by_mask(num: float, accuracy: float) -> float:
    accuracy = str(accuracy)
    accuracy = len(accuracy[accuracy.find('.')+1::])
    return float(f'{pi:0.{accuracy}f}')


d = input("Введите с какой точностью задано число π в фомате 0,001: ")
print(f"При d = {d}, π = {format_by_mask(pi, d)}")


# from math import pi

# def toFixed(pi: float, n=0):
#     a, b = str(pi).split('.')
#     return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))


# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Должно быть введено целое число")
#     return number


# d = InputNumbers("Введите число, определяющее точность числа π (количество знаков после запятой): ")

# print(f"При d = {d}, π = {toFixed(pi, d)}")
