# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

data_1 = open("text_words.txt", "r")
data_2 = open("text_code_words.txt", "a")

def encode (s):
    with open('text_words.txt', 'r', encoding='utf-8') as my_file_1, \
        open('text_code_words.txt', 'a', encoding='utf-8') as my_file_2:
        s = my_file_1.readline()
        encoding = ""
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            encoding += str(count) + s[i]
            i += 1
        my_file_2.write(encoding)
        print("Open the 'text_code_words' file")
        return encoding
s = data_1.readline()
my_encode = encode(s)
print(my_encode)
