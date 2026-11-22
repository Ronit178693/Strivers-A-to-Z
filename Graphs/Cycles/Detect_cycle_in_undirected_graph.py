from collections import deque
# Using BFS Traversal 
def Cycle_detection(v, adj):
    # Visited array for marking the node visited 
    visited = [0] * v     
    q = deque()
    # In case the graph is not connected and is in seperate components
    for start in range(v):
        # If the node is not visited mark it visited and move the node in the queue along with its parent 
        if(visited[start] == 0):
            visited[start] = 1
            # Appending the first element in the the queue with no parent
            q.append((start, -1))
            
            while(q):
                node, parent = q.popleft()
                # Going through all the adj. elements of the node
                for i in adj[node]:
                    # If the node is not visited append it to the queue and mark it visited is it was already visited then we have detected a cycle 
                    if(visited[i] == 0):
                        visited[i] = 1
                        q.append((i, node))
                    elif(i != parent):
                        return True 
    return False

# Using DFS

def Cycle_detection(v, adj):
    # Handlling a visited array. A cycle is detected when a node is visited twice 
    visited = [0] * v
    
    def dfs_helper(start, parent):
        # We are traversing through this element because it is unvisited 
        # Marking the element visited
        visited[start] = 1
        # Now traversing through its adj.
        for i in adj[start]:
            # If the element adj. to the parent is not visited
            if(visited[i] == 0):
                if(dfs_helper(i, start) == True):
                    return True
            elif(i != parent):
                return True
        return False
        
    
    # Handelling seperate components of the same graph if any 
    for start in range(v):
        # If the node is not visited then traverse it and its neighbouring nodes 
        if(visited[start] == 0):
            if(dfs_helper(start, -1) == True):
                return True
    return False
            
        
    
                
            
                
        
        
    
    
    
    
    