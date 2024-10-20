'''
[How good are you really?]

There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.
You receive an array with your peers' test scores.
Now calculate the average and compare your score!
Return true if you're better, else false!

Note:
Your points are not included in the array of your class's points. Do not forget them when calculating the average score.
'''

# def better_than_average(class_points, your_points):
#     pass

def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average

'''
Для решения задачи можно написать функцию, которая будет вычислять средний балл среди одноклассников, включая ваш собственный балл, и затем сравнивать его с вашим баллом.
Если ваш балл выше среднего, функция должна возвращать True, в противном случае — False.

Объяснение:
    Сумма баллов: Мы используем sum(class_points) для вычисления суммы баллов одноклассников.
    Среднее значение: Среднее значение вычисляется как сумма баллов (включая ваш) делённая на общее количество студентов (одноклассники + вы).
    Сравнение: Мы сравниваем ваш балл с вычисленным средним значением. Если ваш балл больше, возвращаем True, иначе — False.
'''
