class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Solution:
    def pairs(self, head, target):
        pairs = []
        if(head is None):
            return pairs
        
            
        current = head
        # To store the nodes we have visited
        seen = set()
        # To store the pairs formed
        
        while(current is not None):
            needed_node_val = target - current.data
            if(needed_node_val in seen):
                pairs.append([needed_node_val, current.data])
            seen.add(current.data)
            current = current.next
        # As we are making pairs when we find the second element so the list pairs is sorted according to them. for a + b = Target and if b > a then a will always be the smaller one so we just reverse it to make the array sorted 
        pairs.reverse()
        return pairs
    
    
# Optimal Solution
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Solution:
    def pairs(self, head, target):
        tail = head 
        pairs = []
        while(tail.next is not None):
            tail = tail.next
        while(head != tail):
            # As its given that the LL is sorted 
            sum = head.data + tail.data
            if(sum > target):
                tail = tail.prev
            elif(sum < target):
                head = head.next
            else:
                pairs.append([head.data, tail.data])
                head = head.next
                tail = tail.prev
        return pairs
                
                
            
    
                
            
            
            
        
        