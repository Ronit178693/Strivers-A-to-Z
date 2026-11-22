from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution :
    def right_view(self, root:list):
        ans = []
        if(root is None):
            return ans
        q = deque()
        q.append(root)
        while(q):
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            right_node = level.pop()
            ans.append(right_node)
        return ans