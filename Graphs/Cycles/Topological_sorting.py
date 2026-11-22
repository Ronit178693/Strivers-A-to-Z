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
        
        
        