'''
[ Calculate average ]

Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.
'''


def find_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)
