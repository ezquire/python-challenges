from collections import deque

def findShortestPath(grid, start, goal):
    visited = {}
    q = deque([(start, 0)])
    while q:
        pos, numMoves = q.popleft()
        visited[pos] = True
        moves = getNextMoves(grid, pos[0], pos[1])
        for move in moves:
            if move[0] == goal[0] and move[1] == goal[1]:
                return numMoves + 1
            if not visited.get(move):
                q.append((move, numMoves + 1))
        
def getNextMoves(grid, sx, sy):
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
        if (x != sx or y != sy):
            nextMoves.append((x, y))
    return nextMoves
    
grid = [[1, 0, 0, 0],
        [1, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0]]
        
grid2 = [[0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0]]
        
print(findShortestPath(grid2, (0, 4), (2, 2)))
