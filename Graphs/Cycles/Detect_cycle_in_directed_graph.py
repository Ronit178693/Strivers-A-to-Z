'''
For directed graph the node has to be revisited on the same path then it is a cycle 
'''

def cycle_detection(v, adj):
    # The visited array to keep the track of all the visited nodes
    visited = [-1] * v
    # The path visited array to keep the track of all the visited paths 
    path_visited = [-1] * v
    
    # The dfs helper function
    def dfs_helper(start):
        # As the node was not visited we mark it and the path visited 
        visited[start] = 1
        path_visited[start] = 1
        # Traversing for the neighbouring nodes 
        for i in adj[start]:
            # If the neighbouring node is not visited then visit it via a recursive dfs call
            if(visited[i] == -1):
                # If any dfs call returns true that iis if any one cycle is detected then keep on returning true
                if(dfs_helper(i) == True):
                    return True
                # The node is already visited, but to be a cycle it has to be on the same path
            elif(visited[i] == 1 and path_visited[i] == 1):
                 # The neighbour is visited ans is on thesame path then cycle is detected andtrue is returned
                return True
        # If none of the condition for that start node evaluates to true that is there is no adj. node present then simply return False and start clearing that path 
        path_visited[start] = 0
        return False
            
        
    
    # Considersing seperate components
    for start in range(v):
        # If the node is not visited then call dfs traversal for that node 
        if(visited[start] == -1):
            # Just return True once a cicle is detected no furter calls needed
            if(dfs_helper(start) == True):
                return True
    return False
            