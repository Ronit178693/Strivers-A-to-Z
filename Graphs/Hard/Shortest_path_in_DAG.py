'''
To find the shortest disteance to every node from the startinf node in a DAG 

1) Do a topo sort on the graph 
2) Take the nodes out of the stack and relax the edges 
'''
def shortest_path(start_node, v, adj):
    # Initiallyy perform the topo sort and populate the stack 
    visited = [-1] * v
    st = []
    def dfs_helper(start):
        visited[start] = 1
        # Targeting only the nodes instead of weights
        for i, j in adj[start]:
            if(visited[i] == -1):
                dfs_helper(i)
        st.append(start)
    for start in range(v):
        if(visited[start] == -1):
            dfs_helper(start)
            
# This topo sort populates the stack 

    dist = [float('inf')] * v
    dist[start_node] = 0
    while(st):
        node = st.pop()
        for neighbor, weight in adj[node]:
            dist[neighbor] = min(dist[node] + weight, dist[neighbor])
    # This gives us the distcance from the starting node to every other node
    return dist
        
                
