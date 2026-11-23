'''
Only exists on DAG

Linear ordering of vertices such that if there is an edge between u and v, u appears befor v in that ordering 
'''

def topological_sort(v, adj):
    # The visited array 
    visited = [-1] * v
    # Handelling connected components
    st = []
    # Helper list for returning the answer 
    ans = []

    def dfs_helper(starting_node):
        # The node was not visited so we will first mark it visited 
        visited[starting_node] = 1
        # also append the element to the stack
 
        # Iterating through the adj. nodes
        for i in adj[starting_node]:
             if(visited[i] == -1):
                 dfs_helper(i)
        st.append(starting_node)
        
    for i in range(v):
        # If the node was not visited visit it 
        if(visited[i] == -1):
            dfs_helper(i)
    # While there are elements in the stack we pop them and store them in an array
    while(st):
        # Popping the top of the stack and storing it 
        ans.append(st.pop())
    return ans 


# Topological Sorting using BFS (Kahns Algo)

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
                
            
            
            
   