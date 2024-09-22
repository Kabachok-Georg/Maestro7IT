'''
[String incrementer]

Your job is to write a function which increments a string, to create a new string.
    1. If the string already ends with a number, the number should be incremented by 1.
    2. If the string does not end with a number. the number 1 should be appended to the new string.

Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''

import re

def increment_string(s):
    # Используем регулярное выражение для поиска числа в конце строки, если оно есть
    match = re.search(r'(\d+)$', s)

    if match:
        # Извлекаем числовую часть и строковую часть до числа
        number = match.group(1)
        prefix = s[:match.start()]

        # Увеличиваем число и сохраняем ведущие нули, используя zfill для исходной длины
        incremented_number = str(int(number) + 1).zfill(len(number))

        return prefix + incremented_number
    else:
        # Если числа в конце строки нет, добавляем '1' в конец
        return s + '1'

# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))
