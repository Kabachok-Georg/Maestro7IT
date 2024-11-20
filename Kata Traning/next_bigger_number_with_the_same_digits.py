'''
[ Next bigger number with the same digits ]

Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.

For example:
  12 ==> 21
 513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):
  9 ==> -1
111 ==> -1
531 ==> -1
'''

def next_bigger(n):
    digits = list(str(n))  # Преобразуем число в список цифр
    length = len(digits)

    # Шаг 1: Найти "уязвимую" цифру
    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1  # Если перестановка невозможна, возвращаем -1

    # Шаг 2: Найти минимальную подходящую цифру справа
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            break

    # Шаг 3: Поменять цифры местами
    digits[i], digits[j] = digits[j], digits[i]

    # Шаг 4: Отсортировать оставшиеся цифры справа
    digits = digits[:i + 1] + sorted(digits[i + 1:])

    # Вернуть результат
    return int("".join(digits))


