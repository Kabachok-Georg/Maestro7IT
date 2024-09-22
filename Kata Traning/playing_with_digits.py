'''
[Playing with digits]

Some numbers have funny properties.

For example:
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :

(ap+bp+1+cp+2+dp+3+...)=n∗k(p+bp+1 +cp+2 +dp+3 +...)=n∗k

If it is the case we will return k, if not return -1.

Note: n and p will always be strictly positive integers.

Examples:
n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1
n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k
n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
'''


def dig_pow(n, p):
    # Преобразуем n в строку и получаем цифры
    digits = [int(d) for d in str(n)]

    # Вычисляем сумму цифр, возведённых в соответствующие степени
    total = sum(d ** (p + i) for i, d in enumerate(digits))

    # Проверяем, делится ли сумма на n
    if total % n == 0:
        return total // n  # Возвращаем k
    else:
        return -1  # Если нет такого k

# def dig_pow(n, p):
#     sum = 0
#     for c in str(n):
#         sum += int(c) ** p
#         p += 1
#     if sum % n == 0:
#         return sum / n
#     else:
#         return -1