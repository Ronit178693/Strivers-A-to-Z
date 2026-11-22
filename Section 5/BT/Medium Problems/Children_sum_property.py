'''
Children sum property = Value(node) = value(node.right) + value(node.left)

If the property is not followed we can increment the value of any node by +1 any number of times

1) Sum the right and the left of the root if sum < root assign both left and right = root and move left 
2) when right and left = Null move back and start traversing the right half similarly to that of the left half
3) when both left and right returns sum them and reassign the node to left + right 
4) if left + right > node then dont change their values 

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def Children_sum(self, root:Node):
        if(root is None):
            return None
        sum = 0
        if(root.left):
            sum += root.left.val
        if(root.right):
            sum += root.right.val
        if(sum < root.val):
            if(root.left):
                root.left.val = root.val
            if(root.right):
                root.right.val = root.val
        self.Children_sum(root.left)
        self.Children_sum(root.right)
        
        total = 0
        if(root.right):
            total += root.right.val
        if(root.left):
            total += root.left.val
        if(root.right or root.left):
            root.val = total
        