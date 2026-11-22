'''
In python Graphs can be represented either by using an Adj. list or by using an Adj. Matrix
An adjacency list is best for sparse graphs to save memory, while an adjacency matrix is ideal for dense graphs that need fast edge lookups.
'''
# Adj. List representation of a graph
from collections import defaultdict 

dict = defaultdict(list)
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
for u, v in edges:
    # Forward pass
    dict[u].append(v)
    dict[v].append(u)
    
# Adj. Matrix representation of a graph
v = 4 #Number of nodes 
matrix = [[0]*v for _ in range(v)] 
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1

    