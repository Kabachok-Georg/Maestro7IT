'''
Task Overview:
Given a non-negative integer n, write a function which returns that number in a binary format as an integer.

Examples:
n = 1 -> 1
n = 5 -> 101
n = 11 -> 1011
'''

def to_binary(n):
    return int(bin(n)[2:])

# Пояснение:
# bin(n) преобразует число n в строку с двоичной записью, начинающуюся с "0b".
# bin(n)[2:] убирает первые два символа ("0b") и оставляет только двоичное представление.
# int(...) преобразует полученную строку двоичных цифр обратно в целое число.

# TODO: Заметки
## Дата: 13.09.2024