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


# TODO: Заметки
## Преподаватель: Дуплей Максим Игоревич
## Дата: 08.10.2024