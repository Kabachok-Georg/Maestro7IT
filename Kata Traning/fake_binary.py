'''

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
8 KUY

'''

def fake_bin(x):
    return ''.join('0' if int(char) < 5 else '1' for char in x)
