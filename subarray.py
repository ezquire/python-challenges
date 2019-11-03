def similar_sub(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    if l1 < l2:
        for i in range(l1, l2):
            arr1.append(0)
    elif l1 > l2:
        for i in range(l2, l1):
            arr2.append(0)
    memo = [[0] * len(arr1) for _ in range(len(arr2))]
    ans = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                if i == 0 or j == 0:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i-1][j-1] + 1
                ans = max(ans, memo[i][j])
    return ans

arr1 = [1, 2, 9, 4, 10, 2, 3, 4, 5, 6, 7, 8, 90, 0, 0, 0]
arr2 = [2, 3, 4, 5, 6, 10, 6, 0, 0, 0, 0] 

print("The longest equivalent subarray is", similar_sub(arr1, arr2), "elements long")

 
