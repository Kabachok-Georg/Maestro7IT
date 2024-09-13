'''
Isograms (7 kyu)

An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''


'''
Функция для определения, является ли строка изограммой (т.е. строкой без повторяющихся букв), может быть реализована следующим образом.
Мы будем игнорировать регистр букв, а пустую строку считать изограммой.

Функция на Python:
```python
def is_isogram(string):
    # Преобразуем строку в нижний регистр, чтобы игнорировать регистр букв
    lower_string = string.lower()
    
    # Преобразуем строку в множество и сравниваем его длину с исходной строкой
    return len(lower_string) == len(set(lower_string))
```

Пояснение:
    Игнорирование регистра:
    Метод lower() преобразует строку в нижний регистр, чтобы не учитывать разницу между заглавными и строчными буквами (например, "A" и "a" считаются одинаковыми).

    Проверка на уникальность:
    Множество (set) в Python хранит только уникальные элементы.
    Преобразуя строку в множество, мы удаляем все повторяющиеся символы.
    Если длина множества совпадает с длиной исходной строки, значит все буквы уникальны.

    Возврат результата:
    Если количество символов в множестве такое же, как в строке, функция возвращает True, что означает, что строка является изограммой.
    В противном случае возвращается False.
'''

def is_isogram(string):
    # Преобразуем строку в нижний регистр, чтобы игнорировать регистр букв
    lower_string = string.lower()

    # Преобразуем строку в множество и сравниваем его длину с исходной строкой
    return len(lower_string) == len(set(lower_string))


# TODO: Заметки
## Дата: 13.09.2024