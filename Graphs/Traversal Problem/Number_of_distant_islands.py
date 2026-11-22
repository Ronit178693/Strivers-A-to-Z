from collections import deque
def islands(grid):
    rows, cols = len(grid), len(grid[0])
    # Visited array for keeping track of the visited cells
    visited = [[0] * cols for _ in range(rows)]
    # For storing all the visited island patterns
    islands = set()
    def bfs(row, col, cords):
        q = deque()
        q.append((row, col))
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited[row][col] = 1
        while(q):
            # Found the first piece of land we will first store it 
            r, c = q.popleft()
            cords.append((r - row, c - col))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # Now we have to check if the neighbour is in the grid and it is not visited and it is a piece of land 
                if(0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0 and grid[nr][nc] == 1):
                    q.append((nr, nc))
                    visited[nr][nc] = 1
    for row in range(rows):
        for col in range(cols):
            # If the cell is a piece of land and is not visited we can start a bfs from there to get the island pattern
            if(grid[row][col] == 1 and visited[row][col] == 0):
                # We have found our first island we have to store the coordinates of the island in the set and then we will move to the next island and store its coordinates in the set and so on
                cords = []
                bfs(row, col, cords)
                # storing the coordinates of the island in the set 
                islands.add(cords)
                # all the islands are now stored in the grid with their coordinates
    return len(islands)
                
'''
Iterate through the grid until you find the first 1. Once the first 1 is found we have found our first island. We then perform bfs traversal from that cell and store the coordinates of that island after subtracting the coordinates of the first cell of the island from all the other cells of the island. This is done so that we can store the island in a unique way and we can compare it with other islands. We then store the coordinates of the island in a set and move to the next island and repeat the process until we have traversed through the whole grid. Finally we return the length of the set which will give us the number of distinct islands in the grid.
'''
