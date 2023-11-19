import time
import random


def bubble_sort(array):
    for i1 in range(len(array)):
        for j in range(len(array)):
            if array[j] > array[i1]:
                tmp = array[j]
                array[j] = array[i1]
                array[i1] = tmp
    return array


avg_imp = 0
avg_my = 0
i = 0
for i in range(101):
    arr = [random.randint(0, 1000) for x in range(100)]
    # function
    start = time.time()
    comp = sorted(arr)
    avg_imp += (time.time() - start)
    # cicle
    start = time.time()
    bubble_sort(arr)
    avg_my += (time.time() - start)
print(f"Среднее время сортировки функции: {avg_imp/i}")
print(f"Среднее время сортировки пузырьком: {avg_my/i}")
