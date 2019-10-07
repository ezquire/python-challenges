import math

def linear_intersect(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1
    return result

def binary_intersect(arr1, arr2):
    result = []
    if len(arr1) < len(arr2):
        short_array = arr1
        long_array = arr2
    else:
        short_array = arr2
        long_array = arr1

    start = 0
    for n in short_array:
        new_start = lower_bound(long_array, start, n)
        if new_start == len(long_array):
            break
        if long_array[new_start] == n:
            result.append(n)
            start = new_start + 1
    return result

def lower_bound(arr, start, target):
    l = start
    h = len(arr)
    while l < h:
        mid = l + (h - l) // 2
        if target <= arr[mid]:
            h = mid
        else:
            l = mid + 1
    return h

def optimal_intersect(arr1, arr2):
    n = len(arr1)
    m = len(arr2)    
    if n <= m:
        if n + m <= n*math.log(m):
            print("Using linear search:")
            return linear_intersect(arr1, arr2)
        else:
            print("Using binary search:")
            return binary_intersect(arr1, arr2)
    if n > m:
        if n + m <= m*math.log(n):
            print("Using linear search:")
            return linear_intersect(arr1, arr2)
        else:
            print("Using binary search:")
            return binary_intersect(arr1, arr2)

arr1 = [5, 1, 2, 1, 1, 2]
arr2 = [1, 2, 2, 4, 5, 9]

arr1.sort()
arr2.sort()

print(optimal_intersect(arr1, arr2))

