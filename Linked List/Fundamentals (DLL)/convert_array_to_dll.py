class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    def conversion(self, array:list) -> Node:
        self.head = Node(array[0])
        current = self.head
        for i in range(1, len(array)):
            newNode = Node(array[i])
            current.next = newNode
            newNode.prev = current
            current = current.next
        return self.head