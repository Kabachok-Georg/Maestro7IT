'''
[ Beginner Series #3 Sum of Numbers ]
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it.
If the two numbers are equal return a or b.
Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.
'''


def get_sum(a, b):
    # Используем min и max для правильного порядка чисел
    return sum(range(min(a, b), max(a, b) + 1))

# get_sum(1, 2)


'''
Нужно найти сумму всех целых чисел между двумя числами 𝑎 и 𝑏, включая их.
Если 𝑎 и b равны, нужно вернуть одно из них.

Пояснение к решению:

- Определение диапазона:
Для того чтобы гарантировать, что числа a и b обрабатываются в правильном порядке (независимо от того, какое из них больше), мы используем функции min(a, b) и max(a, b).
min(a, b) возвращает меньшее из двух чисел (это будет наша начальная точка диапазона).
max(a, b) возвращает большее из двух чисел (это будет конечная точка диапазона).

- Генерация диапазона:
Функция range(start, stop) генерирует последовательность чисел от start до stop-1.
Чтобы включить конечную точку b, используем max(a, b) + 1 в качестве второй границы.
Например, если a=1 и b=3, range(min(1, 3), max(1, 3) + 1) создаст последовательность чисел от 1 до 3: [1,2,3].

- Вычисление суммы:
Функция sum() вычисляет сумму всех чисел в диапазоне, который мы получили с помощью range().
'''
