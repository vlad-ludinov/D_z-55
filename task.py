from need import list_gen

def heaplify(list, heapSize, i):
    largest = i
    left = 2 * i + 1
    rigth = 2 * i + 2

    if left < heapSize and list[left] > list[largest]:
        largest = left
    
    if rigth < heapSize and list[rigth] > list[largest]:
        largest = rigth
    
    if largest != i:
        temp = list[i]
        list[i] = list[largest]
        list[largest] = temp

        heaplify(list, heapSize, largest)


def heap_sorting(list):
    n = len(list)

    for i in range(n, -1, -1):
        heaplify(list, n, i)
    
    for i in range(n - 1, 0, -1):
        temp = list[0]
        list[0] = list[i]
        list[i] = temp

        heaplify(list, i, 0)


list1 = list_gen(-1000, 1000, 20)
print(list1)

heap_sorting(list1)
print(list1)