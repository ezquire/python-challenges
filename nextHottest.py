# Description

# Given a list of daily temperatures A, return a list such that, for each day in A, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# Examples


# Input: A = [73, 74, 75, 71, 69, 72, 76, 73]
#              ^    ^
# Output: [1, 1, 4, 2, 1, 1, 0, 0]. For example, the number of days we'd have to wait to get a hotter day for A[0] is just one day so A[0] = 1. Because the next day at A[1] is hotter than A[0].

# Notes
# Each temperature will be an integer in the range [30, 100]
# The length of temperatures will be in the range [1, 20000]
def nextHottest(arr):
    temps = [0]*len(arr)
    for i, temp in enumerate(arr):
        temps[i] = findNext(arr[i + 1:], temp)
    return temps

def findNext(arr, temp):
    for i in range(len(arr)):
        if arr[i] > temp:
            return i + 1
    return 0
    
A = [73, 74, 75, 71, 69, 72, 76, 73]

B = [76, 75, 74, 73, 72, 71, 70, 69]

print(nextHottest(A))