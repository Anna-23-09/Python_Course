#  Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

line = input()
# list_1 = [int(x.strip(',.*')) for x in line.split() if x.replace("-", "").isdigit()]
list_1 = [x.strip(',.*') for x in line.split() if x.replace("-", "").isdigit()]
print(f'Min: {min(list_1, key=int)}')
print(f'Max: {max(list_1, key=int)}')

# разложенный вариант, выше более концентрированный
list_1 = []
for x in line.split():
    if x.replace("-", "").isdigit():
        list_1.append(x.strip(',.*'))
print(f'Min: {min(list_1, key=int)}')
print(f'Max: {max(list_1, key=int)}')
