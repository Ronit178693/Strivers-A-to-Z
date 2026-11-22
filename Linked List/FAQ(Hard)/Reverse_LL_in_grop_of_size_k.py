# Solution using Stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def reverse(self, head, k):
        # Initializing a stack
        stack = []
        current = head 
        dummyNode = Node(0)
        temp = dummyNode
        while(current is not None):
            stack.append(current)
            current = current.next
            # When the stack size reaches the limit pop all the elements from the stack and add them after the dummy node
            if(len(stack) == k):
                while(stack):
                    node = stack.pop()
                    temp.next = node
                    temp = temp.next
                temp.next = None
        # If there are any elements present in the stack then join them at the end of the new linkedlist as it is 
        if(stack):
            temp.next = stack[0]
        return dummyNode.next

# Optimal Solution without using extra space =, going to reverse the nodes in the group of size k and then joining them together

class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
class LinkedList:
    def length(self, head):
        if(head is None):
            return 0
        count = 0
        current = head
        while(current is not None):
            count += 1
            current = current.next
        return count
    
    def reverse(self, head):
        if(head is None or head.next is None):
            return head
        current = head
        prev = None
        while(current is not None ):
            temp = current.next 
            current.next = prev
            prev = current
            current = temp
        return prev
    
    def reverse_LL(self, head, k):
        if(head is None or head.next is None):
            return head 
        current = head
        count = 0
        while(current is not None):
            
        