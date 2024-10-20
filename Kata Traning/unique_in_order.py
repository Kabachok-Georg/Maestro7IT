'''
Unique In Order

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]


Для решения задачи нам нужно пройти по последовательности элементов и добавить в результат только те элементы, которые отличаются от предыдущего, сохраняя порядок.
Это работает как для строк, так и для списков и кортежей.

Вот функция на Python:

```python
def unique_in_order(sequence):
    # Начинаем с пустого списка для хранения уникальных элементов
    result = []
    
    # Проходим по каждому элементу последовательности
    for i, item in enumerate(sequence):
        # Добавляем элемент в результат, если он отличается от предыдущего
        if i == 0 or item != sequence[i - 1]:
            result.append(item)
    
    return result
```

Пояснение:
Инициализация пустого списка: Сначала мы создаём пустой список result, в который будем добавлять уникальные элементы.
Проход по каждому элементу последовательности: Мы используем цикл for с индексами, чтобы сравнивать текущий элемент с предыдущим.
                                               Если элемент первый в последовательности или отличается от предыдущего, мы добавляем его в результат.
Сохранение порядка: Мы проходим по последовательности в исходном порядке, добавляя только неповторяющиеся подряд элементы.
'''

def unique_in_order(sequence):
    # Начинаем с пустого списка для хранения уникальных элементов
    result = []

    # Проходим по каждому элементу последовательности
    for i, item in enumerate(sequence):
        # Добавляем элемент в результат, если он отличается от предыдущего
        if i == 0 or item != sequence[i - 1]:
            result.append(item)

    return result

print (unique_in_order((1, 2, 2, 3, 3, 4, 5)))

# TODO: Заметки
## Дата: 13.09.2024