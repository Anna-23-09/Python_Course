# Напишите программу, которая на вход принимает 5 чисел и 
# находит максимальное из них.

a = 0
for i in range(5):
    num = int (input())
    if num > a:
        a = num
print(a)