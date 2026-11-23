'''
For directed graph the node has to be revisited on the same path then it is a cycle 
'''
# Using DFS
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
            

# Using BFS
'''
Kahn's algo is not applicable for cyclic directed graphs we are going to detect cycle using that property
'''

from collections import deque
# Initially we are given the adj. list and we have t oconstruct the indegree map using it 
def indegree_table(v, adj):
    # Making an empty table of the same size as of the number of elements 
    indegree = [0] * v
    # This loop populates the indegree table and returns it 
    # Going through all the elements in the adj. list and increeasing their counts 
    for i in adj:
        for j in adj[i]:
            indegree[j] += 1
    return indegree

def Kahns_traversal(v, adj):
    # Calling the indegree_table function to get an indegree table
    indegree = indegree_table(v, adj)
    # Initializing the queue
    q = deque()
    # The list used for returning the answer
    ans = []
    # Going through the map to find out all the initial elements with indegree 0 and appending them to the queue
    for i in range(len(indegree)):
        if(indegree[i] == 0):        
            q.append(i)
    # Iterate through the queue until it got any elements
    while(q):
        # Pop out the top of the queue
        node = q.popleft()
        # Storing the node in the ans
        ans.append(node)
        # Now check for the adj. elements for that node 
        for i in adj[node]:
            # If there are any elements in the adj. list for that node retuce 
            indegree[i] -= 1
            # If the indegree of that respective adj. node turns 0 then push it in the queue
            if(indegree[i] == 0):
                q.append(i)
    return ans
