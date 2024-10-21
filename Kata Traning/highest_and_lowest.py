'''

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples

high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.

'''
# Для вас перевод ниже
'''
В этом небольшом задании вам дана строка чисел, разделенных пробелами, и вам нужно вернуть наибольшее и наименьшее число.

Примеры

high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Примечания

Все номера действительны Int32, нет необходимости их проверять.
Во входной строке всегда будет хотя бы одно число.
Выходная строка должна состоять из двух чисел, разделенных одним пробелом, причем наибольшее число должно быть первым.
'''
#Сначала то чтоб, я сделал

'''def high_and_low(numbers):
    if not numbers:
        return []
    max_num=max(numbers)
    min_num=min(numbers)
    if min_num==[]:
        min_num==0
    return print(max_num, min_num)'''
# Ответ чата  Gpt

def high_and_low(numbers):
    highest = max(numbers)  # Find the highest number
    lowest = min(numbers)  # Find the lowest number
    return f"{highest} {lowest}"  # Return the result as a formatted string

