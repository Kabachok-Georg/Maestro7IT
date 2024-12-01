'''

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3])
# returns [1, 1, 2, 1, 3, 0, 0]

'''


def move_zeros(arr):
    result = [x for x in arr if x != 0]
    result.extend([0] * (len(arr) - len(result)))
    return result

# TODO: Заметки
## Autor: Danilov George
## Date: 01.12.2024