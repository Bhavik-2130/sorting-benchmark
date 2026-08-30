import random
import time

nums = [random.randint(1, 1000) for i in range(10000)]

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

start = time.time()
bubble_sort(nums)
end = time.time()
print("Bubble sort took", end - start, "seconds")

nums2 = [random.randint(1, 1000) for i in range(10000)]
start = time.time()
sorted(nums2)
end = time.time()
print("Python sorted took", end - start, "seconds")