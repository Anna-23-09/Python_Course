# Задайте список из n чисел, заполненный по формуле 
# (1 + 1/n)  n и выведите на экран их сумму.

n = int(input("Введите количество чисел в списке: ")) 
list = []
i = 0
result = 0
for i in range(1, n + 1):
    list.append((1 + 1/n) ** n)
    i += 1
    n = round(n + 1)
    result = result + n
    
print(list)
print(result)

# n = int(input("Введите количество чисел в списке: "))
# list = []

# for i in range(1, n + 1):
#     list.append(round((1 + 1/i) ** i))

# print(list)

# result = 0
# i = 0
# while i < n:
#     result = round(result + i, 0)
#     i = i + 1
# print(result)
