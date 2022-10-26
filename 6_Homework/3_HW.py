# Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, 
# начинающиеся с соответствующей буквы.

s = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

def dict_of_names(tpl):
    names_dict = {}
    for i in tpl:
        name = i[0]
        if name not in names_dict:
            names_dict[name] = i
    return names_dict

ordered_dict = dict_of_names(s)
print(ordered_dict)
