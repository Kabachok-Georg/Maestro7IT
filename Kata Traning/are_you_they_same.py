'''
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples:
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If, for example, we change the first number to something else, comp is not returning true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks:
a or b might be [] or {} (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.

def comp(array1, array2):
    pass
'''

def comp(array1, array2):
    # Проверка на особые случаи, когда один из массивов None или пустой
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False

    # Словарь для подсчета количества квадратов элементов из array1
    count_squares = {}
    for num in array1:
        squared = num ** 2
        if squared in count_squares:
            count_squares[squared] += 1
        else:
            count_squares[squared] = 1

    # Словарь для подсчета количества элементов в array2
    count_elements = {}
    for num in array2:
        if num in count_elements:
            count_elements[num] += 1
        else:
            count_elements[num] = 1

    # Сравнение двух словарей
    return count_squares == count_elements

'''
[Объяснение]

Первоначальная проверка:
    Если один из массивов равен None или длины массивов различны, функция возвращает False.

Подсчет квадратов:
    Для каждого элемента из array1 вычислите его квадрат и обновите количество в словаре count_squares.

Подсчет элементов:
    Аналогично обновите словарь count_elements, который хранит количество каждого элемента в array2.

Сравнение словарей:
    Проверьте, совпадает ли словарь квадратов (count_squares) со словарем элементов (count_elements).
'''