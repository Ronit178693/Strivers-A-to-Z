# BFS traversal in graph 
from collections import deque
# Given the number of nodes and adj list 
def bfs(v:int, adj:dict, starting_node:int):
    result = []
    # Creating the visited array 
    visited = [0] * v
    # Creating the queue for bfs
    q = deque()
    # The queue always starts with the starting node
    q.append(starting_node)
    # The loop goes on until the queue is not empty
    visited[starting_node] = 1
    while(q):
        node = q.popleft()
        result.append(node)
        # Now check for the adj elements int the list and only append them to the queue if they are yet not visited 
        for i in adj[node]:
            if(visited[i] == 0):
                visited[i] = 1
                q.append(i)
    return result
                
def dfs(v:int, adj:dict, node:int):
    
    result = []
    visited = [0] * v
    def dfs_helper(node):
        if(visited[node] != 1):
            visited[node] = 1
            result.append(node)
            for i in adj[node]:
                dfs_helper(i)
        else:
            return 
    dfs_helper(node)
    return result