# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.
  
from math import sqrt


def sqr_r (a, b, c):
    d = b**2 - 4 * a * c
    if a == 0:
        return print('Error')
    with open('sqr.txt', 'a', encoding='utf-8') as my_file:  # создаем и открываем файл
        my_file.write(f'{a}x² + {b}x + {c} = 0\n')
        if d > 0:
            my_file.write(f'{(-b + sqrt(d) / (2 * a))}\n')
            my_file.write(f'{(-b - sqrt(d) / (2 * a))}\n')
        elif d == 0:
            my_file.write(f'{-b / (2 * a)}\n')
        else:
            my_file.write('Нет корней\n')
for i in range(3):
    sqr_r (int(input('a: ')), int(input('b: ')), int(input('c: ')))
    print()
