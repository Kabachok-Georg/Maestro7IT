'''
[ Simplifying multilinear polynomials ]

When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy").
But tell that to your pc and we'll see.

Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):
All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"

All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'.
Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.
'''

from collections import defaultdict
import re  # regex


def simplify(poly):
    # Разбиваем входную строку на отдельные мономы с коэффициентами
    terms = re.findall(r'[+-]?\d*[a-z]+', poly)
    coefficients = defaultdict(int)

    for term in terms:
        # Разделяем на коэффициент и переменные
        match = re.match(r'([+-]?\d*)([a-z]+)', term)
        coeff = int(match.group(1) + "1" if match.group(1) in ["", "+", "-"] else match.group(
            1))  # Приводим коэффициент к числу
        vars = ''.join(sorted(match.group(2)))  # Сортируем переменные в лексикографическом порядке
        coefficients[vars] += coeff  # Складываем коэффициенты для одинаковых переменных

    # Исключаем мономы с нулевыми коэффициентами
    simplified_terms = [(coeff, vars) for vars, coeff in coefficients.items() if coeff != 0]

    # Сортируем мономы: сначала по количеству переменных, затем лексикографически
    simplified_terms.sort(key=lambda x: (len(x[1]), x[1]))

    # Формируем итоговый полином в виде строки
    result = ''.join(
        f"{'+' if coeff > 0 and i > 0 else ''}"  # Добавляем "+" только если коэффициент положительный и это не первый моном
        f"{coeff if abs(coeff) != 1 or not vars else '-' if coeff == -1 else ''}"  # Не пишем "1" или "-1" перед переменными
        f"{vars}"  # Добавляем переменные
        for i, (coeff, vars) in enumerate(simplified_terms)
    )

    return result

'''
Мономы в математике — это элементарные части многочлена, представляющие собой произведение числа (коэффициента) и одной или нескольких переменных, каждая из которых может быть возведена в натуральную степень.
3x — моном, где 3 — коэффициент, а x — переменная.
−5xy — моном, где −5 — коэффициент, x и y — переменные.
2xyz — моном с тремя переменными x, y, z.
'''
