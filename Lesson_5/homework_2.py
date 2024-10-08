'''
[Генератор паролей]

Создание случайных паролей заданной длины с использованием букв, цифр и специальных символов.
'''
import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Введите желаемую длину пароля: "))
generated_password = generate_password(password_length)
print("Ваш сгенерированный пароль:", generated_password)



'''
Шифрование данных (алгоритмы):
1. SHA-256
2. SHA-512
3. MD5
'''

# TODO: Заметки
## Преподаватель: Дуплей Максим Игоревич
## Дата: 08.10.2024