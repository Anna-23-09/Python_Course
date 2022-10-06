# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

n = int(input("N: "))
def factors (n):
    a = 2
    new_list = []  
    while a <= n:
        if n % a == 0:
            new_list.append(a)        
            n //= a
            a = 2
        else:
            a += 1
    print(new_list)

factors(n)
