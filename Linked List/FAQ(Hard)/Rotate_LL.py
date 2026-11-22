class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def length(self, head):
        current = head
        count = 0
        while(current is not None):
            count += 1
            current = current.next
        return count
    def reverse(self, head, k):
        if(head is None or head.next is None):
            return head 
        tail = head 
        temp = head
        while(tail.next is not None):
            tail = tail.next 
        length = self.length(head)
        if(k % length == 0):
            return head
        else:
            rotations = k % length
        count = 1
        while(count <= length - rotations - 1):
            temp = temp.next
            count += 1
        newhead = temp.next
        temp.next = None
        tail.next = head
        return newhead
    
'''
TC - O(N) for finding the length, O(N) for getting the tail and O(length-rotations) for getting the new head 
TC - O(N)
SC - O(1)
'''

               
        