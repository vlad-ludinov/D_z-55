from need import list_gen
from need import algo_time
from need import quick_sort
from need import counting_sort




# получается что сложность быстрой сортировки O(n * log n),
# а от сортировки кучей O(n + k)
# где n это количество элементоов в списке, а k это диапазон значений,
# собственно логично будет что при малом диапозоне значений в списке
# сортировка подсчетом будет выигрывать, но если при большом диапозоне
# быстрая сортировка будет быстрее


# ну, собственно провел некоторое время, поизменял количество нулей,
# вроде как при количестве элементов списка в 40-50 раз меньше чем размер
# диапазона значений, скорость работы этих двух сортировок примерно одинаковая,
# при более чем 50, сортировка подсчетом начинает проигрывать,
# ну и логично обратное, при разнице менее чем в 40 раз быстрая сортировка остает 
 
print('-' * 50)
list1 = list_gen(0,10000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '1')
list1 = list_gen(0,20000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '2')
list1 = list_gen(0,30000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '3')
list1 = list_gen(0,40000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '4')
list1 = list_gen(0,50000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '5')
list1 = list_gen(0,60000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '6')
list1 = list_gen(0,70000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '7')
list1 = list_gen(0,80000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '8')
list1 = list_gen(0,90000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '9')
list1 = list_gen(0,100000,1000)
algo_time(quick_sort, list1)   
algo_time(counting_sort, list1)
print('-' * 50 + '10')
# list1 = list_gen(0,10,100000000)
# algo_time(quick_sort, list1)   #  за 53.175485610961914 сек.
# algo_time(counting_sort, list1)#  за 10.195367813110352 сек.
# print('-' * 50)
# list1 = list_gen(0,100000,100000)
# algo_time(quick_sort, list1)   #  за 0.37835264205932617 сек.
# algo_time(counting_sort, list1)#  за 0.03585505485534668 сек.
# print('-' * 50)
# list1 = list_gen(0,100000000,10)
# algo_time(quick_sort, list1)   #  за 0.0 сек.
# algo_time(counting_sort, list1)#  за 6.6455981731414795 сек.
# print('-' * 50)
