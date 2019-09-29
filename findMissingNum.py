def findMissing(arr, start, end):
    ans = ""
    if start > end:
        return "None"
    if start > arr[-1] or end < arr[0]:
        ans += str(start) + " - " + str(end)
        return ans
    else:
        i = 0
        if start < arr[0]: # capture any range in the beginning
            ans += str(start) + " - " + str(arr[0] - 1)
            start = arr[0]
            i += 1
        while arr[i] <= start: # move i to one past the start
            i += 1
        while i < len(arr) and arr[i] <= end:
            if abs(arr[i] - start) == 2:
                if len(ans) > 0:
                    ans += ", "
                ans += str(start + 1)
            elif abs(arr[i] - start) > 2:
                if len(ans) > 0:
                    ans += ", "
                ans += str(start + 1) + " - " + str(arr[i] - 1)
            start = arr[i]
            i += 1
        
        if end > start: # capture any range at the end
            if len(ans) > 0:
                ans += ", "
            ans += str(start + 1) + " - " + str(end)
    return ans

#      s     e
arr = [1, 3, 5, 7, 8, 9, 13]
#         i 
print(findMissing(arr, 20, 14))   # start > end                                   Output: None
print(findMissing(arr, 14, 20))   # start and end out of bounds at the end        Output: 14 - 20
print(findMissing(arr, -20, 0))   # start and end out of bounds at the beginning  Output: -20 - 0
print(findMissing(arr, -4, 5))    # start out of bounds, end in bounds            Output: -4 - 0, 2, 4
print(findMissing(arr, 5, 20))    # start in bounds, end out of bounds            Output: 6, 10 - 12, 14 - 20
print(findMissing(arr, 5, 12))    # start and end in bounds                       Output: 6, 10 - 12
print(findMissing(arr, -5, 20))   # start and end out of bounds                   Output: -5 - 0, 2, 4, 6, 10 - 12, 14 - 20

