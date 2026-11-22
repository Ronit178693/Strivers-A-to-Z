from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution :
    def bottom_view(self, root:list):
        dic = {}
        if(root is None):
            return []
        q = deque()
        q.append((root, 0))
        while(q):
            node, x = q.popleft()
            if x not in dic:
                dic[x] = []
                dic[x].append(node.val)
            else:
                dic[x].pop()
                dic[x].append(node.val)
                
            if(node.left):
                q.append((node.left, x - 1))
            if(node.right):
                q.append((node.right, x + 1))
        
        ans = []        
        for x in (sorted(dic.keys())):
            ans.extend(dic[x])
                
            
                