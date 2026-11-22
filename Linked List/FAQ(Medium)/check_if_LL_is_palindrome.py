# Brute force solution with TC - O(3N) and SC - O(N)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
class LinkedList:
    def reverse(self, head):
        if(head is None or head.next is None):
            return head
        prev = None
        current = head
        while(current is not None):
            temp = current.next 
            current.next = prev
            prev = current
            current = temp
        return prev
    def check(self, head):
        dummyNode = Node(0)
        temp = dummyNode
        current = head
        while(current is not None):
            newNode = Node(current.data)
            temp.next = newNode 
            temp = newNode
            current = current.next
        dummyNode = dummyNode.next
        reversed_dummyNode = self.reverse(dummyNode)
        while(head is not None):
            if(head.data != reversed_dummyNode.data):
                return False
            head = head.next
            reversed_dummyNode = reversed_dummyNode.next 
        return True
    
# Better solution with TC - O(2N), SC - O(N)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
class LinkedList:
    def palindrome(self, head):
        stack = []
        current = head 
        while(current is not None):
            stack.append(current.data)
            current = current.next 
        temp = head 
        while(temp is not None):
            node = stack.pop()
            if(temp.data != node):
                return False 
            temp = temp.next 
        return True
    
# Optimal Solution using TC O(N) and SC - O(1)
            
        