# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

n = int(input("N: "))
def factors (n):
    list = []
    a = 2
    while n % a == 0 and a <= n:
        list.append(a)
    else:
        a += 1
    return list

print(factors(n))
