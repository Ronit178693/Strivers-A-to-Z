class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def ceil(self, root:Node, x:int):
        # val<=x
        floor = -1
        while(root is not None):
            if(root.data == x):
                floor = root.data
                return floor
            if(root.data > x):
                root = root.left
            else:
                # if(root.data < x) then move right
                floor = root.data
                root = root.right
        return floor