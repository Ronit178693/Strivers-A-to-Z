from collections import deque
def scheduler(v, pre):
    # Forming adj. list from the pre table 
    adj = [[] for _ in range(v)]
    for courses, pres in pre:
        adj[pres].append(courses)
    # Now we have a adj. list for the given stuff in the form of u and v that is u is required for v 
    # We can now perform topo sort to check if its even possible to complete all the courses and also write the order of completion 
    # The indegree array
    indegree = [0] * v
    for i in range(v):
        for j in adj[i]:
            indegree[j] += 1
    q = deque()
    ans = []
    # Appending all the elements with indegree 0 in the queue 
    for i in range(len(indegree)):
        if(indegree[i] == 0):
            q.append(i)
    while(q):
        node = q.popleft()
        ans.append(node)
        for i in adj[node]:
            indegree[i] -= 1
            
            if(indegree[i] == 0):
                q.append(i)
    if(len(ans) == v):
        # Then the courses are completeable and we can return the ans
        return ans
    return []
                
        
    
    