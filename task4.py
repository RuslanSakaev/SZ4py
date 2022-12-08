# 4'. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'.

from functions import create_pol_file
from functions import create_polinom

k = int(input('Введите степень числа: '))

print(f'Сгенерированный полином {create_polinom(k)}')
create_pol_file(create_polinom(k), 'new')
