import time
# sum1 -a +b = sum2 -b +a
# sum1 - sum2 = 2a - 2b
# (sum1 - sum2) / 2 = a - b
# b = a - ((sum1 - sum2) / 2)

def getTarget(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    if(sum1 - sum2) % 2 != 0:
        return None
    return (sum1 - sum2) / 2

def sumswap_sorted(arr1, arr2):
    arr1.sort()
    arr2.sort()
    target = getTarget(arr1, arr2)
    if target == None:
        return None
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        a = arr1[i]
        b = arr2[j]
        diff = a - b
        if diff == target:
            return (a,b)
        elif diff < target:
            i += 1
        else:
            j += 1
    
def sumswap_set(arr1, arr2):
    target = getTarget(arr1, arr2)
    if target == None:
        return None
    set2 = set(arr2)
    for a in arr1:
        b = int(a - target)
        if b in set2:
            return (a,b)

def sumswap_brute_force(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    for a in arr1:
        for b in arr2:
            newSum1 = sum1 - a + b
            newSum2 = sum2 - b + a
            if newSum1 == newSum2:
                return (a,b)
                
arr1 = [5, 1, 2, 1, 1, 2]
arr2 = [3, 6, 3, 3]

t0 = time.process_time()
sumswap_brute_force(arr1, arr2)
t1 = time.process_time()
time_brute = t1 - t0

print("Brute Force Time:", time_brute)

t0 = time.process_time()
sumswap_sorted(arr1, arr2)
t1 = time.process_time()
time_sorted = t1 - t0

print("Sorted Time:", time_sorted)

t0 = time.process_time()
sumswap_set(arr1, arr2)
t1 = time.process_time()
time_set = t1 - t0

print("Set Time:", time_set)
