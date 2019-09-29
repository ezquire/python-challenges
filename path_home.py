def findPath(grid):
    res = []
    dfs(res, [], 0, 0, grid)
    return res

def in_grid(i, j, grid):
    if i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 1:
        return False
    return True

def dfs(res, currentPath, i, j, grid):
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        print("currentPath:", currentPath)
        currentPath.append((i, j))
        res.append(currentPath[:])
        return True
    else:
        currentPath.append((i, j))
        for direction in [(1, 0), (0, 1)]:
            next_i, next_j = i + direction[0], j + direction[1]
            if in_grid(next_i, next_j, grid):
                dfs(res, currentPath, next_i, next_j, grid)
    return False
#        0 1 2 3 4
grid = [[0,0,0,1,1], # 0
        [1,1,0,0,0], # 1
        [1,1,1,0,0], # 2
        [1,1,1,1,0]] # 3

print(findPath(grid))