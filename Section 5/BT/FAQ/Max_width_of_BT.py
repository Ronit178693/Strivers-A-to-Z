'''
width = number of nodes in a level between any 2 nodes 

1) Assign 1 based indexing level wise all accross the tree 
2) subtract the index values of the first and the last node of the tree to get the elements in between the two nodes i.e. the width of the tree

INDEXING 

1) when doing 1 based indexing the right node will have index 2(i) and the left node will have index 2(i)+1

overflow case - incase the tree is scewed and have a large length the indexing that large tree will result in indexoverflow condition
'''
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
class Solution:
    def width(self, root):
        # If there is no tree then there is 0 width
        if(root is None):
            return 0
        max_width = 0
        # The root is already stored in the queue
        queue = deque([(root, 0)])
        while(queue):

            last_indx = queue[-1][1]
            first_indx = queue[0][1]
            
            min_indx = min(last_indx, first_indx)
            
            new_last_indx = last_indx - min_indx
            new_first_indx = first_indx - min_indx
            
            max_width = max(max_width, new_last_indx - new_first_indx + 1)
            
            for i in range(len(queue)):
                node = queue.popleft()
                
                if(node[0].left):
                    queue.append((node[0].left, 2 * node[1] + 1))
                if(node[0].right):
                    queue.append((node[0].right, 2 * node[1] + 2))
        return max_width
                    