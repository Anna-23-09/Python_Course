# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).

n = int(input("Введите число N: ")) 
a = int(input("Введите позицию 1: "))
b = int(input("Введите позицию 2: "))
c = int(input("Введите позицию 3: "))


list = []
i_1 = a - 1
i_2 = b - 1
i_3 = c - 1

result = 1
for i in range(-n + (-1), n):
    list.append(i + 1)
    n += 1

for a in range(-n + (-1), n):      
    for b in range(-n + (-1), n):        
        for c in range (-n + (-1), n):
            if a <= (n * 2) + 1 and b <= (n * 2) + 1 and c <= (n * 2) + 1:
                result
            else:
                print("Error")
print(list)
print(f' {result  * list[i_1] * list[i_2] * list[i_3]}')

