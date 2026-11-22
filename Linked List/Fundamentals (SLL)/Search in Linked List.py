class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinedList:
    def __init__(self):
        self.head = None
    def search(self, element:int):
        current = self.head
        while(current.data != element):
            current = current.next
        return current
