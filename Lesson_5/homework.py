'''
[Фибоначчи до N]

Генерация последовательности Фибоначчи до заданного числа.
'''

def fibonacci_up_to_n(n):
    fib_sequence = []
    a, b = 0, 1
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

print(fibonacci_up_to_n(100))

# TODO: Заметки
## Преподаватель: Дуплей Максим Игоревич
## Дата: --.--.2024