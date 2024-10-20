'''
Написать решение задачи:
Определение процентного соотношения выпадения орла или решки, на ребро.
'''

import random

random_number = random.randint(0, 10000)

if random_number > 0 and random_number%2==0:
    print("Орёл")
elif random_number > 0 and random_number%2!=0:
    print("Решка")
else:
    print("Каким образом тебе выпало ребро?!?! ")