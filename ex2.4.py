import requests
import time
import json
import matplotlib.pyplot as plt
import sys
import random

path = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"



sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    random_index = random.randint(start, end)
    array[start], array[random_index] = array[random_index], array[start]
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high









response = requests.get(path)

new_data = response.json()





input_sizes = []
timings = []

for input_data in new_data:

    input_arr = input_data



    

    input_size = len(input_arr)
    input_sizes.append(input_size)

    start_time = time.time()
    func1(input_arr, 0, input_size - 1)
    end_time = time.time()

    timings.append(end_time - start_time)

print(timings)
plt.plot(input_sizes, timings)
plt.xlabel("Input size")
plt.ylabel("Time taken (seconds)")
plt.show()





