from collections import deque
class Node:
    def __init__(self, val):
        self.val = self.val
        self.left = None
        self.right = None
class Solution:
    def Zig_Zag(self, root):
        if(root is None):
            return []
        '''
        0 - L-R
        1 - R-L
        '''
        flag = 0
        ans = []
        q = deque()
        q.append(root)
        while(q):
            level = []
            n = len(q)
            if(flag == 0):
                for i in range(n):
                    node = q.popleft()
                    level.append(node.val)
                    if(node.left != None):
                        q.append(node.left)
                    if(node.right != None):
                        q.append(node.right)
                ans.append(level)
                flag = 1
            else:
                for i in range(n):
                    node = q.pop()
                    level.append(node.val)
                    if(node.right != None):
                        q.appendleft(node.right)
                    if(node.left != None):
                        q.appendleft(node.left)
                ans.append(level)
                flag = 0
        
        return ans
                
        
        