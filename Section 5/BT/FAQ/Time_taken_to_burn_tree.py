from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def parent_map(self, root):
        if(root is None):
            return 
        # Storing the root node in the queue
        queue = deque()
        queue.append(root)
        # Initializing a hash to store all the parent nodes 
        hashi = {root: None}
        # Populates the hash with all the parent child pairs
        while(queue):
            for i in range(len(queue)):
                node = queue.popleft()
                if(node.left):
                    queue.append(node.left)
                    hashi[node.left] = node
                if(node.right):
                    queue.append(node.right)
                    hashi[node.right] = node
        return hashi
    
    def finding(self, root, start):
        if(root is None):
            return None
        # Pointitn to the root node and we will stop once our pointer points the start node 
        if(root.val == start):
            return root 
        # DFS traversal
        # If the node is found on the left side return the root node 
        left = self.finding(root.left, start)
        if(left):
            return left
        # Else if its not found in the left side it will be on the right side 
        return self.finding(root.right, start)
    
    def time_taken(self, root, start):
        if(root is None):
            return 
        start_node = self.finding(root, start)
        counter = 0
        seen = {start_node}
        queue = deque()
        queue.append(start_node)
        parents = self.parent_map(root)
        while(queue):
            destroyed = False
            for i in range(len(queue)):
                node = queue.popleft()
                            
                if(node.right is not None and node.right not in seen):
                    seen.add(node.right)
                    queue.append(node.right)
                    destroyed = True
                if(node.left and node.left not in seen):
                     seen.add(node.left)
                     queue.append(node.left)
                     destroyed = True
                if(parents[node] is not None and parents[node] not in seen):
                      seen.add(parents[node])
                      queue.append(parents[node])
                      destroyed = True
            # If any node got destroyed then increase the timer 
            if(destroyed == True):
                counter += 1
        return counter
        
        