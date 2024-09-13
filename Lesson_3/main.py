from plus import plus
from minus import minus
from umn import umn
from delit import delit

sigh=input("Введите знак для выполнения желаемого вами действия ")
if sigh=='+':
    print(plus(f_num=int(input("Введите первое число ")),s_num=int(input("Введите второе число "))))
elif sigh=='-':
    print(minus(f_num=int(input("Введите первое число ")),s_num=int(input("Введите второе число "))))
elif sigh=='*':
    print(umn(f_num=int(input("Введите первое число ")),s_num=int(input("Введите второе число "))))
elif sigh=='/':
    print(delit(f_num=int(input("Введите первое число ")),s_num=int(input("Введите второе число "))))
else:
    print('Неверный символ')




















































'''


'''