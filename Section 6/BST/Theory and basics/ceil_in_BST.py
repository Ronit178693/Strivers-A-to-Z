class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def ceil(self, root:Node, x:int):
        # val>=x
        '''
        case 1) when the ceil of x exists 
        
        case 2) when the ceil of x does not exists return None
        '''
        ceil = -1
        while(root != None ):
            if(root.data == x):
                ceil = root.data
                return ceil
            if(root.data < x):
                root = root.right
            else:
             # root.data > x then ceil = root.data
             ceil = root.data
             root = root.left
        return ceil       