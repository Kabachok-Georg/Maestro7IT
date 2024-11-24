'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand

Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''

def zero(op=None): return 0 if op is None else op(0)
def one(op=None): return 1 if op is None else op(1)
def two(op=None): return 2 if op is None else op(2)
def three(op=None): return 3 if op is None else op(3)
def four(op=None): return 4 if op is None else op(4)
def five(op=None): return 5 if op is None else op(5)
def six(op=None): return 6 if op is None else op(6)
def seven(op=None): return 7 if op is None else op(7)
def eight(op=None): return 8 if op is None else op(8)
def nine(op=None): return 9 if op is None else op(9)

def plus(right): return lambda left: left + right
def minus(right): return lambda left: left - right
def times(right): return lambda left: left * right
def divided_by(right): return lambda left: left // right


# TODO: Заметки
## Дата: 24.11.2024
