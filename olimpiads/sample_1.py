'''

# Ввод данных
n = int(input())
a = int(input())

# Количество полос, которые нужно пройти
k = n // a

# Длина ломаной
length = 4 * a * (k - 1) + 2 * a

# Вывод результата
print(length)

'''


# Ввод данных
n = int(input())
a = int(input())

print(n**2-(a*n+a*n-a**2))
