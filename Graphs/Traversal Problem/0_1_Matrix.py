# Nearest 1
from collections import deque
# We are going to use BFS only for this soution as we have to traverse through the neighbours of the elements one by one and this is not possible in DFS
def matrix(mat):
    rows, cols = len(mat), len(mat[0])
    # 2D array for marking cells as visited
    visited = [[0] * cols for _ in range(rows)]
    # Resultant matrix for returning the answer
    result = [[0] * cols for _ in range(rows)]
    q = deque()
    distance = 0
    

    for row in range(rows):
        for col in range(cols):
            # If the cell is 1 and is not visited
            if(mat[row][col] == 1 and visited[row][col] == 0):
                visited[row][col] = 1
                q.append((row, col, distance))
                # All the initial 1's are in the queue now 
                
                
    # Now the BFS traversal on the elements 
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while(q):
        r, c, d = q.popleft()
        result[r][c] = d
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            if(0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0 and mat[nr][nc] == 0):
                q.append((nr, nc, d + 1))
                visited[nr][nc] = 1
                
    return result
                
                
# Nearest 0

def matrix(mat):
    rows, cols = len(mat), len(mat[0])
    # 2D array for marking cells as visited
    visited = [[0] * cols for _ in range(rows)]
    # Resultant matrix for returning the answer
    result = [[0] * cols for _ in range(rows)]
    q = deque()
    distance = 0
    for row in range(rows):
        for col in range(cols):
            # If the cell is 0 and is not visited
            if(mat[row][col] == 0 and visited[row][col] == 0):
                visited[row][col] = 1
                q.append((row, col, distance))
                # All the initial 0's are in the queue now        
    # Now the BFS traversal on the elements 
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while(q):
        r, c, d = q.popleft()
        result[r][c] = d
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            if(0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0 and mat[nr][nc] == 1):
                q.append((nr, nc, d + 1))
                visited[nr][nc] = 1     
    return result