from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if(root is None):
            return ''
        s = ''
        queue = deque()
        queue.append(root)
        while(queue):
            for i in range(len(queue)):
                node = queue.popleft()
                if(node is not None):
                    queue.append(node.left)
                    queue.append(node.right)
                if(node == None):
                    s += '#,'
                else:
                    s += str(node.val) + ','
                
        return s
                
    def deserialize(self, data):
        if(len(data) == 0):
            return None
        # First convert the string to a list seperated by , 
        st = data.split(',')
        i = 0
        root = TreeNode(int(st[i]))
        queue = deque()
        queue.append(root)
        i += 1
        while(queue):
            node = queue.popleft()

            if(st[i] == '#'):
                node.left = None
                i += 1
            else:
                leftNode = TreeNode(int(st[i]))
                node.left = leftNode
                queue.append(leftNode)
                i += 1
               
            if(st[i] == '#'):
                node.right = None
                i += 1
            else:
                rightNode = TreeNode(int(st[i]))
                node.right = rightNode
                queue.append(rightNode)
                i += 1
        return root
        

        
        
        
