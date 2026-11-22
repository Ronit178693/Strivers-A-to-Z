class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def deletion(self, head, key):
        if(head is None):
            return head
        if(head.next is None):
            head = None
            return head
        current = head
        previous = None
        while(current is not None):
            if(current.data == key):
                # If the node is the head node
                if(current.prev is None):
                    previous = current
                    current = current.next
                    head = current
                    current.prev = None
                # If the node is the tail node
                elif(current.next is None):
                    previous.next = None
                    current = None
                # If the node is in between 
                else:
                    previous.next = current.next
                    current = previous.next
                    current.prev = previous     
            else:
                previous = current
                current = current.next
        return head
                    
                