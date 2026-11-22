class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def search(self, root, x):
        while(root != None and root.data != x):
            if(root.data < x):
                root = root.left
            else:
                root = root.right 
        return root