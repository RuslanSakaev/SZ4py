# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Например:
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

from functions import create_polinom
from functions import create_pol_file
from sympy import simplify

degree = int(input('Задайте степень: '))

pol1 = create_polinom(degree) #Генерируем полином
pol2 = create_polinom(degree)

filename1 = 'first'
filename2 = 'second'
sum_filename = 'sum'

create_pol_file(pol1, filename1) #Создаём файлы с полиномом
create_pol_file(pol2, filename2)

with open(f'{filename1}.txt', 'r') as f1: #Считываем из файла информацию
    f_pol = f1.read()
    print(f'Первый полином: {f_pol}')

with open(f'{filename2}.txt', 'r') as f2:
    s_pol = f2.read()
    print(f'Второй полином: {s_pol}')

sum_of_pols = simplify(f_pol + '+' + s_pol) #Складываем полиномы
sum_of_pols = str(sum_of_pols)

print(f'Сумма: {sum_of_pols}')

with open(f'{sum_filename}.txt', 'w') as s: #Записываем в фаил
    s.write(sum_of_pols)

