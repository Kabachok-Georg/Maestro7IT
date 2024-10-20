'''
[Is this a triangle?]

Implement a function that accepts 3 integer values a, b, c.
The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

Examples:
Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false
'''

# def is_triangle(a, b, c):
#     return False

def is_triangle(a, b, c):
    # Проверяем, что стороны положительные и удовлетворяют неравенству треугольника
    return a > 0 and b > 0 and c > 0 and (a+b>c) and (b+c>a) and (a+c>b)

'''
Условия:
1. and
2. or
3. not (!=)
'''