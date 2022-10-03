# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def new_list (size):
    list_of_numbers = sample(range(1, 11), size)
    return list_of_numbers

def sum_num (my_list):  
    sum_numbers = my_list[0]
    k = len(my_list) 
    for i in range(2, k, 2):
        sum_numbers += my_list[i]
    return sum_numbers

k = int(input("Введите длину списка: "))
list_num = new_list(k)
print(list_num)
print(sum_num(list_num))
