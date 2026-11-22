
from collections import defaultdict


class Solution:
    # Making the adj. list
    def adj_list(self, n, edges):
        dict = defaultdict(list)
        for u, v in edges:
            dict[u].append(v)
            dict[v].append(u)
        return dict 

    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = self.adj_list(n, edges)
        visited = [0] * n
        count = 0
        def dfs(node, comp):
            if(visited[node] == 0):
                # Mark the node as visited
                visited[node] = 1
                comp.append(node)
                for i in adj[node]:  
                    dfs(i, comp)
            else:
                return 
        for i in range(len(visited)):
            # If the node is not visited then travers through it using DFS traversal algo 
            if(visited[i] == 0):
                comp = []
                dfs(i, comp)
                is_complete = True
                # Now check if the traversed sub graph is completed or not
                for i in comp:
                    # For the graph to be complete every node in the dfs traversal should be adj to all the other nodes of the graph
                    if(len(adj[i]) != len(comp) - 1):
                        is_complete = False
                        break
                   
                if(is_complete == True):
                    count += 1
        return count

        