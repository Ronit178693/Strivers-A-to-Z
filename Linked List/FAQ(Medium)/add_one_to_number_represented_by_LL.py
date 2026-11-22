class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    # First reverse the linkedlist then add 1 to it 
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
    def add_one(self, head):
        current = self.reverse(head)
        dummyNode = Node(-1)
        temp = dummyNode

        add = 1
        carry = 0
        while(current is not None or carry != 0):
            sum = 0
            val = current.data if current is not None else 0
                
            sum = val + add + carry
            if(add == 1):
                add -= 1
            if(carry != 0):
                carry = 0
            node_value = sum%10
            carry += sum//10
            
            newNode = Node(node_value)
            temp.next = newNode
            temp = newNode
            if(current is not None):
                current = current.next
        dummyNode = dummyNode.next 
        return self.reverse(dummyNode)