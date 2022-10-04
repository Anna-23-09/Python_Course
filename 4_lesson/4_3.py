# Задайте два числа. Напишите программу, которая найдёт
# НОК (наименьшее общее кратное) этих двух чисел.

from math import gcd
a = int(input("a = : "))
b = int(input("b = : "))
print(a * b // gcd(a, b))
print(gcd(a, b))