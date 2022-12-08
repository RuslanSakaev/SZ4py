import sympy
from random import randint as rnd

def create_polinom(k: int, simple: bool = True) -> str: #генерирует полином со случайными коэффициэнтами степени К, simple = False вернёт полином без сокращения нулевых коэффицентов
    polinom = ''
    for i in range(k, -1, -1):
        polinom += f'{rnd(0,2)}*x**{i}+'
        if i == 0:
            polinom += f'{rnd(0,100)}*x**{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)

def create_pol_file(polinom: str, filename: str = 'new'): #Записывает полином в фаил, дополнительно можно указать имя файла
    with open(f'{filename}.txt', 'w') as f: # f'SZ4PY/{filename}.txt' указываем путь, если хотим указать паку записи файла, инчае файл запишется в корневую папку
        f.write(polinom)
