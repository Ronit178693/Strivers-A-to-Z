class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        current = self.head
        
        result = []
        while(current is not None):
            result.append(current.data)
            current = current.next
         
        return result