'''
Bipartite graph is a graph which can be coloured with 2 colours where no adj. nodes have the same colour 

Linear graphs with no cycle are always bipertite

Any graph with even cycle length can also be bipetite

Graphs with odd ycle length cant be bipetite
'''


# Using BFS Traversal
from collections import deque

def bipetiite(graph):
    # The array keeping track of the colors
    color_map = [-1] * len(graph) 
    for i in range(len(color_map)):
        # If the node is not colored then color it 
        if(color_map[i] == -1):
            # Appending the first node in the queue 
            q = deque()
            q.append(0)
            # And marking its color
            color_map[0] = 0
            # Changing the color
    
            # Performing BFS Traversal
            while(q):
                # Taking the node ot of the queue
                node = q.popleft()
                # Append the adj. nodes in the queue and also change their color in color map
                for adj_nodes in graph[node]:
                    # If the node is already visited that is it was already colored then we wont consider it 
                    if(color_map[adj_nodes] == -1):
                        # This lefts us all the nodes which are not visited 
                        # Append those elements in the queue and change the color
                        q.append(adj_nodes)
                        color_map[adj_nodes] = 1 - color_map[node]
                    # If the node was already colored we check if the two node have same color or not 
                    elif(color_map[node] == color_map[adj_nodes]):                    
                        return False
 
        # This changes the value of color between 0 and 1    
    return True

    
# Using DFS Traversla
def bipetite(graph):
    color_map = [-1] * len(graph)
    def dfs_helper(node, color):
        # That is the node was never visited till now 
        # Color the unvisited node and then traverse through the adj. nodes 
            color_map[node] = color 
            for i in graph[node]:
                if(color_map[i] == -1):
                    # If even a one DFS calls returns False that is the graph is not bipetite then all the other calls also returns False
                    if(dfs_helper(i, color = 1 - color) == False):
                        return False
                elif(color_map[i] == color_map[node]):
                    return False 
            return True
    # Safety check for connected components
    for start in range(len(graph)):
        # If the node is not yet colored
        if(color_map[start] == -1):
            if(dfs_helper(start, 0) == False):
                return False
    return True
            
        
    
            
    
