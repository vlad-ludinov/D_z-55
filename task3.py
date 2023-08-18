from random import randint
from need import list_gen
from need import rand_list_gen
from need import algo_time
from need import quick_sort
from need import counting_sort
from need import binary_search

def choice_sort(list):
    range_list = max(list) - min(list)
    len_list = len(list)
    if range_list / len_list <= 50:
        return counting_sort
    else:
        return quick_sort


list1 = rand_list_gen()
print(list1)
original_list = list1.copy()
print(original_list)
sort_list = choice_sort(list1)(list1)
print(sort_list)


