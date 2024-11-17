'''

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

'''


def find_uniq(arr):
    # Use multiple results to produce unique results
    unique_values = set(arr)

    # Checking how many unique values are in the set
    if len(unique_values) == 2:
        # If two values are unique then we can find them
        for num in unique_values:
            if arr.count(num) == 1:
                return num

