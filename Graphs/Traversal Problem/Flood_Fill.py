from collections import deque
def floodFill(image, sr, sc, color):
    # Storing the initial cell colour for matching 
    starting_cell = image[sr][sc]
    rows, cols = len(image), len(image[0])
    # Creating a visited 2D array
    visited = [[0] * cols for _ in range(rows)]
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1
    image[sr][sc] = color
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while(q):
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # After gettig the neighbours coordinate 
                
            if(0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0 and image[nr][nc] == starting_cell):
                q.append((nr, nc))
                visited[nr][nc] = 1
                image[nr][nc] = color
    return image
            
        