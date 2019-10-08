def equiv_subarray(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    if l1 < l2:
        for i in range(l1, l2):
            arr1.append(0)
    elif l2 < l1:
        for i in range(l2, l1):
            arr2.append(0)
    memo = [[0]*l1 for _ in range(l2)]
    ans = 0
    for i in range(l1):
        for j in range(l2):
            if arr1[i] == arr2[j]:
                if j == 0 or i == 0:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i-1][j-1] + 1
                    ans = max(ans, memo[i][j])
    return ans


arr1 = [1, 2, 3, 100, 7, 8]
arr2 = [1, 2]

print(equiv_subarray(arr1, arr2))
