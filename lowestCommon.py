def lowestCommon(array):
    if len(array) == 0:
        return None
    if len(array[0]) == 0:
        return None
    common = list(set(array[0])) # strip duplicates
    for i in range(1, len(array)):
        current = list(set(array[i])) # strip duplicates
        if len(current) == 0:
            return None
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(common) and pointer2 < len(current):
            if common[pointer1] < current[pointer2]:
                common.pop(0)
                if len(common) == 0:
                    return None
            elif current[pointer2] < common[pointer1]:
                pointer2 += 1
                if pointer2 == len(current):
                    return None
            else:
                pointer1 += 1
                pointer2 += 1
    return common[0]

def lowestCommon2(array):
    if len(array) == 0:
        return None
    if len(array[0]) == 0:
        return None
    common = set(array[0])
    for i in range(1, len(array)):
        if len(array[i]) == 0:
            return None
        common = common.intersection(set(array[i]))
    smallest = float("inf")
    for num in common:
        if num < smallest:
            smallest = num
    return smallest if smallest != float("inf") else None

def lowestCommon3(array):
    if len(array) == 0:
        return None
    common = array[0]
    for i in range(1, len(array)):
        pointer1 = 0
        pointer2 = 0
        temp_common = []
        arr = array[i]
        while pointer1 < len(common) and pointer2 < len(arr):
            if common[pointer1] < arr[pointer2]:
                pointer1 += 1
            elif arr[pointer2] < common[pointer1]:
                pointer2 += 1
            else:
                temp_common.append(arr[pointer2])
                pointer1 += 1
                pointer2 += 1
        common = temp_common
    return common[0] if common else None

arr1 = [[1, 3, 5, 10, 20], [2, 4, 5, 10, 20], [2, 4, 10, 20]]
arr2 = [[1, 3, 5, 10, 20], [2, 4, 5, 10, 20], [30, 40]]
arr3 = [[1, 3, 5, 10, 20], [2, 4, 5, 10, 20], [2, 4]]
arr4 = [[1, 2 ,3], [1, 2, 3]]
arr5 = [[1, 2], [3, 4, 5, 30]]
arr6 = [[1, 3, 10]]
arr7 = [[1, 2, 3], []]
arr8 = []
arr9 = [[]]
arr10 = [[], [1, 2, 3]]
arr11 = [[1, 2, 2, 2, 2, 2, 2, 3], [1, 2, 3, 3, 3]]

#print("Expected: 10   |", "Actual:", lowestCommon(arr1))
#print("Expected: None |", "Actual:", lowestCommon(arr2))
#print("Expected: None |", "Actual:", lowestCommon(arr3))
#print("Expected: 1    |", "Actual:", lowestCommon(arr4))
#print("Expected: None |", "Actual:", lowestCommon(arr5))
#print("Expected: 1    |", "Actual:", lowestCommon(arr6))
#print("Expected: None |", "Actual:", lowestCommon(arr7))
#print("Expected: None |", "Actual:", lowestCommon(arr8))
#print("Expected: None |", "Actual:", lowestCommon(arr9))
#print("Expected: None |", "Actual:", lowestCommon(arr10))
#print("Expected: 1    |", "Actual:", lowestCommon(arr11))
# common
# [5, 10, 20]
#  ^
# current
# [2, 4, 5, 10, 20]
#        ^ 

# print("Expected: 10   |", "Actual:", lowestCommon2(arr1))
# print("Expected: None |", "Actual:", lowestCommon2(arr2))
# print("Expected: None |", "Actual:", lowestCommon2(arr3))
# print("Expected: 1    |", "Actual:", lowestCommon2(arr4))
# print("Expected: None |", "Actual:", lowestCommon2(arr5))
# print("Expected: 1    |", "Actual:", lowestCommon2(arr6))
# print("Expected: None |", "Actual:", lowestCommon2(arr7))
# print("Expected: None |", "Actual:", lowestCommon2(arr8))
# print("Expected: None |", "Actual:", lowestCommon2(arr9))
# print("Expected: None |", "Actual:", lowestCommon2(arr10))
# print("Expected: 1    |", "Actual:", lowestCommon2(arr11))

print("Expected: 10   |", "Actual:", lowestCommon3(arr1))
print("Expected: None |", "Actual:", lowestCommon3(arr2))
print("Expected: None |", "Actual:", lowestCommon3(arr3))
print("Expected: 1    |", "Actual:", lowestCommon3(arr4))
print("Expected: None |", "Actual:", lowestCommon3(arr5))
print("Expected: 1    |", "Actual:", lowestCommon3(arr6))
print("Expected: None |", "Actual:", lowestCommon3(arr7))
print("Expected: None |", "Actual:", lowestCommon3(arr8))
print("Expected: None |", "Actual:", lowestCommon3(arr9))
print("Expected: None |", "Actual:", lowestCommon3(arr10))
print("Expected: 1    |", "Actual:", lowestCommon3(arr11))