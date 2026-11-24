from collections import deque

def shortest_path(start_node, v, adj):
    dist = [float('inf')] * v
    q = deque()
    q.append((start_node, 0))
   
    dist[start_node] = 0
    while(q):
        node, dis = q.popleft()
        for i in adj[node]:
            if(dist[i] > dis + 1):
                dist[i] = dis + 1
                q.append((i, dist[i]))
    return dist
            