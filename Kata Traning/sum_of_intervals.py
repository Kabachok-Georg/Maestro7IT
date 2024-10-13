'''
Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the interval lengths.
Overlapping intervals should only be counted once.

[ Intervals ]
Intervals are represented by a pair of integers in the form of an array.
The first value of the interval will always be less than the second value.
Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

[ Overlapping Intervals ]
List containing overlapping intervals:
[
   [1, 4],
   [7, 10],
   [3, 5]
]

The sum of the lengths of these intervals is 7.
Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:
sumIntervals( [
   [1, 2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1, 4],
   [7, 10],
   [3, 5]
] ) => 7

sumIntervals( [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030

[ Tests with large intervals ]
Your algorithm should be able to handle large intervals.
All tested intervals are subsets of the range [-1000000000, 1000000000].
'''


def sum_of_intervals(intervals):
    # Сортируем интервалы по их началу
    intervals.sort(key=lambda x: x[0])

    # Переменная для хранения объединенных интервалов
    merged_intervals = []

    # Проходим по каждому интервалу
    for interval in intervals:
        # Если список пуст или текущий интервал не пересекается с последним добавленным интервалом
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(list(interval))  # Преобразуем кортеж в список и добавляем его
        else:
            # Иначе объединяем перекрывающиеся интервалы
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

    # Теперь считаем сумму длин всех объединенных интервалов
    return sum(interval[1] - interval[0] for interval in merged_intervals)


# print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)

