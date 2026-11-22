# Optimal Solution with TC : O(N/2) the brute forece solution manually finds the length first then finds mid 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def deletion(self, head):
        if(head is None):
            return head
        if(head.next is None):
            head = None
            return head
        if(head.next.next is None):
            head.next = None
            return head
        slow, fast = head, head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        slow.data = slow.next.data
        slow.next = slow.next.next
        return head
        
            
            
        