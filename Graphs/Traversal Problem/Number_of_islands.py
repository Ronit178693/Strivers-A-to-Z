from collections import deque

# Using BFS Traversal
def islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    visited = [[0] * cols for _ in range(rows)]
    
    def bfs(row, col):
        q = deque()
        q.append((row, col))
        visited[row][col] = 1
        # The directions in which we have to move 
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        while(q):
            r, c = q.popleft()
            # Finding the neighbours
            for i, j in dirs:
                # Got the cooordinates of all the neighbours now just check if they are land and if they are visited 
                neighbour_r, neighbour_c = r + i, c + j
                # Handle the bound errors in this condition
                if(0 <= neighbour_r < rows and 0 <= neighbour_c < cols and grid[neighbour_r][neighbour_c] == '1' and visited[neighbour_r][neighbour_c] == 0):
                    visited[neighbour_r][neighbour_c] = 1
                    q.append((neighbour_r, neighbour_c))

    for row in range(rows):
        for col in range(cols):
            # If the cell is land but it was not visited then increment the counter as we have found one island and then traverse through the island using BFS traversal algo
            if(grid[row][col] == '1' and visited[row][col] == 0):
                count += 1 
                bfs(row, col)
    return count
                
    
    
# Using DFS Traversal


def islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    visited = [[0] * cols for _ in range(rows)]
    
    def dfs(row, col):
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        # That is the land is not yet visited
        if(0 <= row < rows and 0 <= col < cols and visited[row][col] == 0 and grid[row][col] == '1'):
            # Then first mark it as visited 
            visited[row][col] = 1
            # Now move to all the neighbours one by one using a loop 
            for r, c in dirs:
                dfs(row + r, col + c)
        else:
            return 

    for row in range(rows):
        for col in range(cols):
            # If the cell is land but it was not visited then increment the counter as we have found one island and then traverse through the island using BFS traversal algo
            if(grid[row][col] == '1' and visited[row][col] == 0):
                count += 1 
                dfs(row, col)
    return count
                
    