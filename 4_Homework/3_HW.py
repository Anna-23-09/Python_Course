# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности в том же порядке.

from itertools import count

def get_uniq_nums (list_num):
    uniq_num = []
    for i in list_num:
        count = list_num.count(i)
        if count == 1:
            uniq_num.append(i)
    return uniq_num

list_num = [ 5, 7, 3, 3, 2, 3, 8, 1, 154, 245, 8, 4, 2, 0]
print(list_num)
new_list = get_uniq_nums(list_num)
print(new_list)   
