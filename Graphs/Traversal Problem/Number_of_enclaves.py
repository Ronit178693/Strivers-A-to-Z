from collections import deque
def enclaves(grid):
    rows, cols = len(grid), len(grid[0])
    # Making a visited array 
    visited = [[0] * cols for  _ in range(rows)]
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # We will initially mark all the boundary cells as visited 
    q = deque()
    for c in range(cols):
        # Finding all the boundary elements on the top boundary
        if(grid[0][c] == 1 and visited[0][c] == 0):
            q.append((0, c))
            visited[0][c] = 1
        # Finding all the boundary elements on the bottom on the grid
        if(grid[rows - 1][c] == 1 and visited[rows - 1][c] == 0):
            q.append((rows - 1, c))
            visited[rows - 1][c] = 1
    for r in range(rows):
        # Boundary elements on the left boundary
        if(grid[r][0] == 1 and visited[r][0] == 0):
            q.append((r, 0))
            visited[r][0] = 1
        if(grid[r][cols - 1] == 1 and visited[r][cols - 1] == 0):
            q.append((r, cols - 1))
            visited[r][cols - 1] = 1
    while(q):
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if(0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0 and grid[nr][nc] == 1):
                visited[nr][nc] = 1
                q.append((nr, nc))
    # So far we have mared all the boundary and boundary related elements on the visited 2D list now the ones only left are the non boundary ones 
    count_visited = 0
    count_real = 0
    for row in range(rows):
        for col in range(cols):
            if(visited[row][col] == 1):
                count_visited += 1
            if(grid[row][col] == 1):
                count_real += 1
    return count_real - count_visited
            
        
    
    