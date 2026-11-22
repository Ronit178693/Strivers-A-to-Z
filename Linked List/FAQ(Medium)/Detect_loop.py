# Brute Force solution
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    
    def loop(self, head):
        seen = set()
        current = head 
        while(current is not None):
            if(current in seen):
                return True
            seen.add(current)
            current = current.next
        return False
            
            
# Optimal Solution avoiding the extra space being used
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def loop (self, head):
        slow, fast = head, head 
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next 
            if(fast == slow):
                return True
        return False