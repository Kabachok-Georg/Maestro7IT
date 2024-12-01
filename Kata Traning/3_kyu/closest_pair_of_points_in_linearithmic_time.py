'''
[ Closest pair of points in linearithmic time ]

Given a number of points on a plane, your task is to find two points with the smallest distance between them in linearithmic O(n log n) time.

Example:
  1  2  3  4  5  6  7  8  9
1
2    . A
3                . D
4                   . F
5             . C
6
7                . E
8    . B
9                   . G

For the plane above, the input will be:
(
  (2,2), # A
  (2,8), # B
  (5,5), # C
  (6,3), # D
  (6,7), # E
  (7,4), # F
  (7,9)  # G
)
=> closest pair is: ((6,3),(7,4)) or ((7,4),(6,3))
(both answers are valid. You can return a list of tuples too)
The two points that are closest to each other are D and F.
Expected answer should be an array with both points in any order.

Goal:
The goal is to come up with a function that can find two closest points for any arbitrary array of points, in a linearithmic time.
Note: Don't use math.hypot, it's too slow...
'''


import math


# Функция для вычисления расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Функция для нахождения ближайшей пары точек в полосе
def closest_in_strip(strip, d):
    min_dist = d
    strip.sort(key=lambda p: p[1])  # Сортируем по y-координате
    closest_pair = None
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            d = dist(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
                closest_pair = (strip[i], strip[j])
    return closest_pair


# Рекурсивная функция для нахождения ближайшей пары точек
def closest_pair_util(points_x, points_y):
    if len(points_x) <= 3:
        min_dist = float('inf')
        closest_pair = None
        for i in range(len(points_x)):
            for j in range(i + 1, len(points_x)):
                d = dist(points_x[i], points_x[j])
                if d < min_dist:
                    min_dist = d
                    closest_pair = (points_x[i], points_x[j])
        return closest_pair

    mid = len(points_x) // 2
    mid_point = points_x[mid]

    # Разделяем точки на левую и правую половину
    left_x = points_x[:mid]
    right_x = points_x[mid:]
    left_y = [p for p in points_y if p[0] <= mid_point[0]]
    right_y = [p for p in points_y if p[0] > mid_point[0]]

    # Рекурсивно находим ближайшую пару в каждой половине
    left_pair = closest_pair_util(left_x, left_y)
    right_pair = closest_pair_util(right_x, right_y)

    # Определяем минимальное расстояние между ближайшими парами
    left_dist = dist(left_pair[0], left_pair[1])
    right_dist = dist(right_pair[0], right_pair[1])
    min_dist = min(left_dist, right_dist)

    # Выбираем пару с минимальным расстоянием
    if min_dist == left_dist:
        closest_pair = left_pair
    else:
        closest_pair = right_pair

    # Проверяем наличие ближайшей пары в полосе
    strip = [p for p in points_y if abs(p[0] - mid_point[0]) < min_dist]
    strip_pair = closest_in_strip(strip, min_dist)

    # Если в полосе найдено более близкое расстояние, обновляем пару
    if strip_pair:
        return strip_pair

    return closest_pair


# Основная функция для нахождения ближайшей пары точек
def closest_pair(points):
    points_x = sorted(points, key=lambda p: p[0])  # Сортируем по x-координате
    points_y = sorted(points, key=lambda p: p[1])  # Сортируем по y-координате
    return closest_pair_util(points_x, points_y)


# TODO: Заметки
## Autor: Danilov George
## Date: 30.11.2024
