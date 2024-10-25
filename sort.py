import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

input_list = [64, 34, 25, 12, 22, 11, 90]


start_time = time.time()
bubble_sorted = bubble_sort(input_list.copy())
bubble_sort_time = time.time() - start_time

start_time = time.time()
insertion_sorted = insertion_sort(input_list.copy())
insertion_sort_time = time.time() - start_time


print( bubble_sorted)
print( insertion_sorted)
print( bubble_sort_time)
print( insertion_sort_time)
