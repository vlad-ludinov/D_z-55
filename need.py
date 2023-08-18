from random import randint
from time import time

def list_gen(mi=-5, ma=5, le=10):
    return [randint(mi, ma) for i in range(le)]

def algo_time(func, x):
    start = time()
    func(x)
    finish = time() - start
    print(f'Выполнение за {finish} сек.')