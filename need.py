from random import randint
from time import time

def list_gen(mi=-5, ma=5, le=10):
    return [randint(mi, ma) for i in range(le)]

def rand_list_gen():
    mi = randint(-100000, -1000)
    ma = randint(1000, 100000)
    le = randint(1000, 1000000)
    return list_gen(mi, ma, le)

def algo_time(func, x):
    start = time()
    func(x)
    finish = time() - start
    print(f'Выполнение за {finish} сек.')

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = list(filter(lambda x: x < pivot, lst))
    center = [i for i in lst if i == pivot]
    right = list(filter(lambda x: x > pivot, lst))
    return quick_sort(left) + center + quick_sort(right)


def counting_sort(list):
    max_item = max(list)
    min_item = min(list)
    lst=[0 for _ in range(max_item - min_item + 1)]
    for i in list:
        lst[i - min_item] = lst[i - min_item]+1
    res_list = []
    for i in range(len(lst)):
        if lst[i]:
            res_list.extend([i + min_item] * lst[i])
    return res_list

def binary_search(lst, value, left, right):
    if right < left:
        return None
    middle_point = (right - left) // 2 + left
    if lst[middle_point] < value:
        return binary_search(lst, value, middle_point + 1, right)
    elif lst[middle_point] > value:
        return binary_search(lst, value, left, middle_point - 1)
    else:
        return middle_point