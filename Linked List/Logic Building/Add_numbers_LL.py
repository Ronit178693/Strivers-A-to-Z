# The only solution to the problem is this optimal solution with TC - O(max(l1, l2)) and SC - O(N) 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def add_numbsers(self, l1, l2):
        # Creating the dummy node 
        dummyNode = Node()
        temp = dummyNode
        carry = 0
        while(l1 is not None or l2 is not None or carry is not 0):
            sum = 0
            if(l1 is not None):
                sum += l1.data
                l1 = l1.next
            if(l2 is not None):
                sum += l2.data
                l2 = l2.next
            if(carry is not 0):
                sum += carry
                carry = 0
            # Increment carry
            carry += sum//10
            node_data = sum % 10
            newNode = Node(node_data)
            temp.next = newNode
            temp = newNode
        current = dummyNode
        dummyNode = dummyNode.next
        current = None
        return dummyNode

            
        