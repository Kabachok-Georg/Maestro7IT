'''

There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required for all the customers to check out!

input: customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.

output: The function should return an integer, the total time required.

Important:
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

Examples:
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
'''

import heapq


def queue_time(customers, n):
    if not customers:  # Если клиентов нет
        return 0

    if n == 1:  # Если только одна касса, то время — это сумма всех времен
        return sum(customers)

    tills = [0] * n  # Инициализируем массив касс, где каждая касса имеет начальное время 0

    for customer in customers:  # Обрабатываем каждого клиента
        min_time_till = heapq.heappop(tills)  # Получаем кассу с минимальным временем
        heapq.heappush(tills, min_time_till + customer)  # Обновляем время этой кассы

    return max(tills)  # Возвращаем максимальное время из всех касс


'''
Функция queue_time(customers, n) рассчитывает общее время, необходимое для того, чтобы все клиенты в очереди прошли через кассы самообслуживания.
Каждый клиент занимает некоторое время, и кассы свободны по мере того, как на них заканчивается время.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
heapq: Мы используем стандартный модуль Python heapq, чтобы поддерживать список касс в отсортированном порядке, что позволяет эффективно находить и обновлять кассу с минимальным временем.

Куча (min-heap): В куче хранятся значения времени, когда каждая касса будет свободна.
                 Это позволяет быстро находить кассу, которая освободится первой.

Время: Ожидаемая сложность — O(k log n), где k — количество клиентов, а n — количество касс.
       Для каждого клиента мы выполняем задачи с кучей (heappop и heappush), которые занимают время O(log n).
'''
