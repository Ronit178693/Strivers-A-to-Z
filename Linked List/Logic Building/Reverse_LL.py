class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinekdList:
    def reverse(self, head):
        # Case 1) If the LinkedList is empty
        if(head is None):
            return None
        # Case 2) If the LL only have single element
        if(head.next is None):
            return head
        # Case 3) More elements 
        prev = None
        current = head 
        while(current is not None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev