def minFallingPath(arr):
    m = len(arr)
    n = len(arr[0])
    
    dp = [[0 for i in range(n)] for j in range(2)]
    for i in range(n):
        dp[0][i] = arr[0][i]
        
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[1][j] = min(dp[0][j], dp[0][j + 1]) + arr[i][j]
            elif j == n - 1:
                dp[1][j] = min(dp[0][j], dp[0][j - 1]) + arr[i][j]
            else:
                dp[1][j] = min(dp[0][j - 1], dp[0][j], dp[0][j + 1]) + arr[i][j]
        dp[0] = dp[1]
    return min(dp[-1])

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
       
arr2 = [[-10, 5, 2], 
        [-1, -2, 3]]

print(minFallingPath(arr))
