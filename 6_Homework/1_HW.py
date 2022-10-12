# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

first_list = [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]

def more_value(list: first_list):
    final_list = [first_list[i] for i in range(1, len(first_list)) if first_list[i] > first_list[i - 1]]
    return final_list

answer_list = more_value(first_list)
print(answer_list)
