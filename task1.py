from need import list_gen

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


list1 = list_gen(-10, 10, 20)
print(list1)
print()

print(counting_sort(list1))