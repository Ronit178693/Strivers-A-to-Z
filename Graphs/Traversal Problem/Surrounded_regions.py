from collections import deque
def regions(grid):
    rows, cols = len(grid), len(grid[0])
    # Making a visited 2D array to keep track of the visited cells
    visited = [[0] * cols for _ in range(rows)]
    # We will first move through the boundaries of the the grid and make all the O's safe including their regions 
    # Traversing through the top and the bottom boundaries 
    
    def bfs(row, col):
        q = deque()
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        q.append((row, col))
        visited[row][col] = 1
        while(q):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # Now we have to check if the neighbour is in the grid and it is not visited and it is O 
                if(0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0 and grid[nr][nc] == 'O'):
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    
    for col in range(cols):
        # If the cell on the top boundary is O and it is not visited 
        if(grid[0][col] == 'O' and visited[0][col] == 0):
            bfs(0, col)
        # If the cell on the bottom boundary is O and it is not visited
        if(grid[rows - 1][col] == 'O' and visited[rows - 1][col] == 0):
            bfs(rows - 1, col)
        # As  we have marked all the O's at top and on the bottom we will mark the X's as visited in thoes rows 
        if(grid[0][col] == 'X' and visited[0][col] == 0):
            visited[0][col] = 1
        if(grid[rows - 1][col] == 'X' and visited[rows - 1][col] == 0):
            visited[rows - 1][col] = 1
    # Traversing through the left and the right boundaries
    for row in range(1, rows - 1):
        if(grid[row][0] == 'O' and visited[row][0] == 0):
            bfs(row, 0)
        if(grid[row][cols - 1] == 'O' and visited[row][cols - 1] == 0):
            bfs(row, cols - 1)
        if(grid[row][0] == 'X' and visited[row][0] == 0):
            visited[row][0] = 1
        if(grid[row][cols - 1] == 'X' and visited[row][cols - 1] == 0):
            visited[row][cols - 1] = 1
    # Now we are done with all the safe O's all that is left is to traverse through the grid and make all the unsae one s to X's
    for row in range(rows):
        for col in range(cols):
            if(grid[row][col] == 'O' and visited[row][col] == 0):
                grid[row][col] = 'X'