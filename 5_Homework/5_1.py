# Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.

n = int(input("Enter the length of string: "))

from random import choices, sample

def list_rand_words(n: int, alp: str = 'абв'):
    words_list = []
    for i in range(n):
        letters = sample(alp, 3)
        words_list.append("".join(letters))
    return words_list

list_of_words = list_rand_words(n)
print(list_of_words)

def delete_of_some_strings (list_of_words):
    wrong_text = 'абв'
    for i in list_of_words:
        if i != wrong_text:
            list_of_words.append(i)
    return list_of_words

print(delete_of_some_strings(list_of_words))
