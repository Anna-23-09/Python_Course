# 3. Напишите программу, которая будет на вход принимать число N и 
# выводить числа от -N до N

a = int(input("Введите число N: "))

for i in range(-a, a + 1):
    print(i, end=" ")
