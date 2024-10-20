'''
[The observed PIN]

Alright, detective, one of our colleagues successfully observed our target person, Robby the robber.
We followed him to a secret warehouse, where we assume to find all the stolen stuff.
The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally).
E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks.
You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations?
It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits.
We could name the function getPINs (get_pins in python, GetPINs in C#).
But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you
'''

# def get_pins(observed):
#     pass # TODO: This is your job, detective

'''
Чтобы решить задачу генерации всех возможных вариантов ПИН-кода на основе соседних цифр, можно следовать этим шагам:
    Определить раскладку клавиатуры: Можно представить клавиатуру в виде словаря, где каждая цифра сопоставлена со своими соседними цифрами (включая саму себя).
    Сгенерировать комбинации: Для каждой цифры в введенном ПИН-коде мы найдем все возможные цифры (саму цифру и соседние). Затем мы создадим все возможные комбинации этих цифр.
    Вернуть результаты: Наконец, вернем комбинации в виде списка строк.
'''

from itertools import product


def get_pins(observed):
    # Определяем раскладку клавиатуры
    adjacent_digits = {
        '0': ['0'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }

    # Создаем список возможных цифр для каждой цифры в введенном ПИН-коде
    possible_digits = [adjacent_digits[digit] for digit in observed]



    # Преобразуем каждую комбинацию из кортежа в строку
    return [''.join(combination) for combination in all_combinations]

'''
[] Пояснение:
   Раскладка клавиатуры: Мы определяем словарь adjacent_digits, где каждый ключ — это строка, представляющая цифру, а значение — список строк, представляющий саму цифру и её соседние цифры.
   Поиск возможных цифр: Мы проходим по каждой цифре в введенном ПИН-коде и создаем список возможных цифр, используя раскладку клавиатуры.
   Генерация комбинаций: Используем itertools.product, чтобы создать все комбинации возможных цифр. Это даст нам декартово произведение списков.
   Форматирование результатов: Наконец, мы соединяем каждую кортеж из цифр в строку и возвращаем список всех возможных вариантов ПИН-кода.

[] Для ввода '1357' эта функция сгенерирует варианты, такие как:
   1357, 1358, 1367, 1368, ...
   1457, 1458, ...
   и так далее.
'''