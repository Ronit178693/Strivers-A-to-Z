# Brute solution using O(N) TC and O(N) SC 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def segregate(self, head):
        dummyNode_even = Node()
        dummyNode_odd = Node()
        temp_odd = dummyNode_odd
        temp_even = dummyNode_even
        index = 'odd' 
        while(head is not None):
            if(index == 'odd'):
                newNode_odd = Node(head.data)
                temp_odd.next = newNode_odd
                temp_odd = newNode_odd
                index = 'even'
            elif(index == 'even'):
                newNode_even = Node(head.data)
                temp_even.next = newNode_even
                temp_even = newNode_even
                index = 'odd'
            head = head.next
        current_even = dummyNode_even
        current_odd = dummyNode_odd
        dummyNode_even = dummyNode_even.next
        dummyNode_odd = dummyNode_odd.next
        current_even = None
        current_odd = None
        temp_odd.next = dummyNode_even
        return dummyNode_odd

# Optimal Solution without using the extra space 


'''
Break the single linkedlist in 2 seperate linkedlists internally then join them
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
class LinkedList:
    def segmentation(self, head):
        # When the linked list got no, 1 or 2 elements only
        if(head is None or head.next is None or head.next.next is None):
            return head
        odd = head
        even = head.next
        even_head = even
        while(even.next is not None and even is not None):
            odd.next = even.next
            odd = even.next
            
            even.next = odd.next
            even = odd.next
        odd.next = even_head
        
        return head
        
                
        