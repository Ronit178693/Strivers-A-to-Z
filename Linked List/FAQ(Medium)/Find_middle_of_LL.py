# Brute Force Solution using O(N+N/2) TC and constant SC 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def middle(self, head):
        if(head is None or head.next is None):
            return head
        if(head.next.next is None):
            return head.next
        current = head
        def Length(current):
            count = 0
            while(current is not None):
                count += 1
                current = current.next
            return count
        length = Length(current)
        mid = (length//2) + 1
        i = 1
        while(i < mid):
            current = current.next
            i += 1
        return current
    
# Optimal Solution : Trying to avoid the N/2 TC 

'''
Using 2 pointers fast and slow 
fast moves 2 steps at a time and slow moves only 1 at a time so by the time fast reaches none or on the end node of the linkedlist slow reaches the middle 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def middle(self, head):
        if(head is None or head.next is None):
            return head
        if(head.next.next is None):
            return head.next
        slow, fast = head, head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow