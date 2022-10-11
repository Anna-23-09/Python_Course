# Реализуйте калькулятор

actions = {
"^": lambda x, y: str(float(x) ** float(y)),
"*": lambda x, y: str(float(x) * float(y)),
"/": lambda x, y: str(float(x) / float(y)),
"+": lambda x, y: str(float(x) + float(y)),
"-": lambda x, y: str(float(x) - float(y))
}

example_1 = "-2 + ( 4 / ( 2 - 7 ) + 8 * 7 ) * 3"

example_2 = '8 + 2 * 4 + ( 6 + ( 2 - 3 * 7 + ( 77 - 11 ) ) * 2 )'

def find_priority (numbers: list):
    new_numbers = []
    i = 0
    while i < len(numbers):
        if numbers[i] == '(':
            if '(' in numbers[i + 1:]:
                numbers = numbers[: i +1] + find_priority (numbers[i + 1:]) # [: i + 1] означает ОТ НАЧАЛА ДО i + 1
            g = numbers.index(')', i)
            new_numbers.append(numbers[i + 1: g]) # [i + 1: g] означает от i + 1 до g
            # таким образом вписали в новый список то, что находится между '(' и ')'
            i = g
        else:
            new_numbers.append(numbers[i])
        i += 1
    return new_numbers

changed_list_1 = find_priority(example_1.split())
print(changed_list_1)
changed_list_2 = find_priority(example_2.split())
print(changed_list_2)


def calc (numbers: list):
    for i, num in enumerate (numbers):
        if isinstance (num, list):
            numbers[i] = calc(num)
    new_list = [x for x, sym in enumerate(numbers) if sym in '*/']
    while new_list:
        k = new_list[0]
        a, b, c = numbers[k - 1: k + 2]
        numbers.insert(k - 1, actions[b](a, c))
        del numbers[k: k + 3]
        new_list = [x for x, sym in enumerate(numbers) if sym in '*/']
    while len(numbers) > 1:
        a, b, c = numbers[:3]
        del numbers[:3]
        numbers.insert(0, actions[b](a, c))
    return numbers[0]


print(calc(changed_list_1))
print(calc(changed_list_2))
