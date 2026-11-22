#  if two nodes overlap take the smaller node first 
from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def verticle_traversal(self, root:list):
        dic = {}
        if(root is None):
            return []
        q = deque()
        #  Storing node, vertical order, level order for a node in the queue
        q.append((root, 0, 0))
        while(q):
            node, x, y = q.popleft()
            '''
                nodes = {
                    x_coordinate: {
                        y_coordinate: [list, of, node, values]
                    }
                }

            '''
            if x not in dic:
                # If x is not in dict create a sub dictonary for x as a key
                dic[x] = {}
            if y not in dic[x]:
                dic[x][y] = []
            dic[x][y].append(node.val)
            
            if(node.left is not None):
                q.append((node.left, x - 1, y + 1))
            if(node.right is not None):
                q.append((node.right, x + 1, y + 1))
        ans = []       
        for x in sorted(dic.keys()):
            temp = []
            for y in sorted(dic[x].keys()):
                temp.extend(sorted(dic[x][y]))
            ans.append(temp)
        return ans 
