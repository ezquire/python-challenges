def mergearrays(arr1, arr2):
    res = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        elif arr2[j]< arr1[i]:
            res.append(arr2[j])
            j += 1
        else:
            res.append(arr1[i])
            res.append(arr2[j])
            i += 1
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res

arr1 = [1, 3, 4, 5] 
arr2 = [2, 4, 6, 8]

print(mergearrays(arr1, arr2))
