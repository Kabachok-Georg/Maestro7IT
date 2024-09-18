'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    pass
'''

'''
Для решения задачи нахождения "цифрового корня" числа нужно суммировать все его цифры и повторять процесс до тех пор, пока результат не станет однозначным числом.

Мы можем решить эту задачу двумя способами:
1. Рекурсией, суммируя цифры числа до тех пор, пока результат не станет однозначным.
2. С использованием математической формулы для цифрового корня.
'''

# Рекурсивное решение задачи:
def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(int(digit) for digit in str(n)))

'''
Объяснение:
1. Если число уже меньше 10, возвращаем его как результат (оно уже однозначное).
2. В противном случае разбиваем число на цифры, суммируем их и снова вызываем `digital_root` для полученной суммы.
'''