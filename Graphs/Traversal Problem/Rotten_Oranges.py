from collections import deque
def oranges(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[0] * cols for _ in range(rows)]
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    timer = 0
    q = deque()
    # Firstly we have to locate the rotten orange 
    # There can me more then one rotten oranges in the start
    for row in range(rows):
        for col in range(cols):
            if(grid[row][col] == 2):
                visited[row][col] = 1
                q.append((row, col, 0))
                
    while(q):
        r, c, t = q.popleft()
        timer = max(timer, t)

        for dr, dc in dirs:
            # Coordinates for the neighbours
            nr, nc = r + dr, c + dc
            
            # while moving to the neighbours neighbours must be anything but not 0 and 2
            if(0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0 and grid[nr][nc] != 2 and grid[nr][nc] != 0):
                # If all the conditions are passing then we are surely landing on a fresh orange 
                q.append((nr, nc, t + 1))
                visited[nr][nc] = 1
                # The timer only increments when we rot a fresh orange
        
    # Now we have to check if there are any fresh oranges left or not
    for row in range(rows):
        for col in range(cols):
            if(grid[row][col] == 1 and visited[row][col] == 0):
                return -1
    return timer
                