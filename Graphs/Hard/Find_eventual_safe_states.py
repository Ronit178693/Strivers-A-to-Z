'''
The node is Considered to be safe only when it does not forms any cycle as we can traverse to any node from the starting node and reach the terminal node the terminal node cant be reached only when a cycle is formed 
'''
# We will simply check for each and every path for each and every node is the node has even a single terminal path then it is considered in our answer

def safe(graph):
    # Number of nodes in the graph
    v = len(graph)
    # Visited array for keeping track of visited elements 
    visited = [-1] * v
    # for keeping track of visited paths 
    visited_path = [-1] * v
    # Helper list for returning the answer
    ans = []
    def dfs_helper(start):
        visited[start] = 1
        visited_path[start] = 1
        for i in graph[start]:
            if(visited[i] == -1):
                # If a cycle is detected for even a single path then we dont have to look for more paths 
                if(dfs_helper(i) == True):
                    return True
                # We have encountered a node repeating
            elif(visited[i] == 1 and visited_path[i]== 1):
                return True
        visited_path[start] = 0
        return False
    # Go through all the nodes if there are any connected component
    for start_node in range(v):
        if(visited[start_node] == -1):
            # If the cycle is not formed then append the node inside the ans list
            dfs_helper(start_node)
        if(visited_path[start_node] == 0):
            ans.append(start_node)  
    return ans
            
            
            
            
    