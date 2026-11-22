# Optimal Solution

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def flattening(self, list):
        values = []
        for _ in list:
            horizontal = _
            while(horizontal is not None):
                values.append(horizontal.data)
                horizontal = horizontal.next
        values.sort()
        dummyNode = Node(-1)
        temp = dummyNode
        i = 0
        while(i < len(values)):
            node = Node(values[i])
            temp.next = node
            temp = temp.next
            i += 1  
            
        return dummyNode.next
    
# Brute Force solution using merging of two sorted linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def merging(self, head1, head2):
        if(head1 is None):
            return head2
        if(head2 is None):
            return head1
        current1, current2 = head1, head2
        dummyNode  = Node(-1)
        temp = dummyNode
        while(current1 is not None and current2 is not None):
            if(current1.data > current2.data):
                temp.next = current2
                current2 = current2.next
                temp = temp.next
            elif(current1.data <= current2.data):
                temp.next = current1
                current1 = current1.next
                temp = temp.next
        while(current1 is not None):
            temp.next = current1
            temp = temp.next
            current1 = current1.next
        while(current2 is not None):
            temp.next = current2
            temp = temp.next 
            current2 = current2.next
        dummyNode = dummyNode.next
        return dummyNode    
    def Flattening(self, list):
        if (len(list) == 0):
            return None
        if(len(list) == 1):
            return list[0]
        
        head1 = list[0]
        for i in range(1, len(list)):
            head1 = self.merging(head1, list[i])
        return head1
    
    
    
'''
# Flattening a Linkedlist
'''
