'''
[ Beginner - Reduce but Grow ]

Given a non-empty array of integers, return the result of multiplying the values together in order.
Example:
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''

def grow(arr):
    result = 1
    for num in arr:
        result *= num  # Multiply each number to the result
    return result
