# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def new_list (size):
    list_of_numbers = sample(range(1, 11), size)
    return list_of_numbers

def prod_of_pairs (my_list):
    list_of_prods = []
    s = len(my_list)
    for i in range(s // 2):
        list_of_prods.append(my_list[i] * my_list[s - i - 1])
    if s % 2:
        list_of_prods.append(my_list[s // 2])
    return list_of_prods
s = int(input("Введите длину списка: "))
list_num = new_list(s)
print(list_num)
print(prod_of_pairs(list_num))
