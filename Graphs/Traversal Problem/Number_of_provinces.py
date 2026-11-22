from collections import defaultdict
class Solution:

    def adj_list(self, isConnected):
        adj = defaultdict(list)
        for rows in range(len(isConnected)):
            for cols in range(len(isConnected[0])):
                if(isConnected[rows][cols] == 1 and rows != cols):
                    adj[rows + 1].append(cols + 1)
                    adj[cols + 1].append(rows + 1)
        return adj

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        adj = self.adj_list(isConnected)
        visited = [0] * (len(isConnected) + 1)
        count = 0

        def dfs(node):
            # That is the node is not visited
            if(visited[node] == 0):
                # Then visit it
                visited[node] = 1
                for i in adj[node]:
                    dfs(i)
            else:
                return

        for i in range(1, len(visited)):
            if(visited[i] == 0):
                count += 1
                dfs(i)
        return count
