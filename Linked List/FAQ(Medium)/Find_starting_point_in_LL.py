# Brute Force solution using TC - O(N) and SC - O(N)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def loop(self, head):
        if(head is None or head.next is None):
            return None
        seen = set()
        current = head
        while(current is not None):
            if(current not in seen):
                seen.add(current)
            else:
                return current
            current = current.next
        return None
    
# Optimal Solution, this solution eliminates the use of extra space
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def loop(self, head):
        if(head is None or head.next is None):
            return None
        slow, fast = head, head
        # 1) Detect the loop
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                break
        if(fast == slow):    
            slow = head
            while(slow != fast):
                slow, fast = slow.next, fast.next
            return slow    
        return None