'''
[Beginner Series #2 Clock]

Clock shows h hours, m minutes and s seconds after midnight.
Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000

Input constraints:
0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
'''

# def past(h, m, s):
#     # Good Luck

def past(h, m, s):
    return (h * 60 * 60 * 1000) + (m * 60 * 1000) + (s * 1000)

'''
Объяснение:

ℎ × 60 × 60 × 1000
h × 60 × 60 × 1000: часы переводятся в миллисекунды (1 час = 3600000 миллисекунд).

𝑚 × 60 × 1000
m × 60 × 1000: минуты переводятся в миллисекунды (1 минута = 60000 миллисекунд).

𝑠 × 1000
s × 1000: секунды переводятся в миллисекунды (1 секунда = 1000 миллисекунд).

Все значения суммируются, и результат возвращается.
'''
