# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

n = int(input("Enter the N: "))

def find_some_nums(n):
    i = 20
    answer_list = [i for i in range(i, n) if i <= n and i % 20 == 0 or i % 21 == 0]
    return answer_list

res = find_some_nums(n)
print(res)
