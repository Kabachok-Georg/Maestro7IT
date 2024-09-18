'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.


def get_count(sentence):
    pass
'''
# a = ['a', 'e', 'i', 'o', 'u']
#
# def get_count(sentence):
#     for i in sentence:
#         if i in a:
#             print(i, end="")
# print()

def get_count(sentence):
    vowels = "aeiou"  # Определяем гласные
    return sum(1 for char in sentence if char in vowels)

