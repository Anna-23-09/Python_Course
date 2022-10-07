# 1. В файле находится N натуральных чисел, записанных через пробел.
#    Среди чисел не хватает одного, чтобы выполнялось условие
#    A[i] - 1 = A[i-1]. Найдите это число.

from random import choice

def fill_list (count: int):
    my_list = [x for x in range(count + 1)]
    my_list.remove(choice(my_list))
    return my_list

new_list = fill_list(int(input('Enter the count: ')))
print(new_list)

def find(my_list: list):
    for i in range(1, len(my_list)):
        if my_list[i] - 1 != my_list[i-1]:
            return my_list[i] - 1
    return -1

print(find(new_list))
