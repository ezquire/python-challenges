def findShortestPath(grid, sx, sy, dx, dy):
    distance = [[float("inf") for x in range(len(grid[0]))] for y in range(len(grid))] 
    distance[sx][sy] = 0
    dfs(grid, sx, sy, distance)
    return distance[dx][dy] if distance[dx][dy] != float("inf") else -1 
    
def getNextMoves(grid, sx, sy, distance):
    nextMoves = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direct in directions:
        x = sx
        y = sy
        while x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid) and grid[x][y] == 0:
            x += direct[0]
            y += direct[1]
        x -= direct[0]
        y -= direct[1]
        if (x != sx or y != sy) and distance[x][y] > distance[sx][sy]:
            nextMoves.append((x, y))
    return nextMoves
    
def dfs(grid, sx, sy, distance):
    nextMoves = getNextMoves(grid, sx, sy, distance)
    for move in nextMoves:
        distance[move[0]][move[1]] = min(distance[sx][sy] + 1, distance[move[0]][move[1]])
        dfs(grid, move[0], move[1], distance)
            
grid = [[1, 0, 0, 0],
        [1, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0]]
        
grid2 = [[0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0]]
        
print(findShortestPath(grid2, 3, 2, 2, 2))
