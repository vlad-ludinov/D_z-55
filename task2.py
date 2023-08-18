from need import list_gen
from need import algo_time

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


# ну, получается что сложность быстрой сортировки O(n * log n),
# а от сортировки кучей O(n + k)
# где n это количество элементоов в списке, а k это диапазон значений,
# собственно логично будет что при малом диапозоне значений в списке
# сортировка подсчетом будет выигрывать, но если при большом диапозоне
# быстрая сортировка будет быстрее

print('-' * 50)
list1 = list_gen(0,10,10)
algo_time(quick_sort, list1)
algo_time(counting_sort, list1)
print('-' * 50)
list1 = list_gen(0,10,100000000)
algo_time(quick_sort, list1)
algo_time(counting_sort, list1)
print('-' * 50)
list1 = list_gen(0,100000,100000)
algo_time(quick_sort, list1)
algo_time(counting_sort, list1)
print('-' * 50)
list1 = list_gen(0,100000000,10)
algo_time(quick_sort, list1)
algo_time(counting_sort, list1)
print('-' * 50)