class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def sort(self, head):
        values = []
        current = head
        while(current is not None):
            values.append(current.data)
            current = current.next
        values.sort()
        dummyNode = Node(0)
        temp = dummyNode
        i = 0
        while(i < len(values)):
            newNode = Node(values[i])
            temp.next = newNode
            temp = temp.next
            i+=1
        return dummyNode.next
    
# Sort list using Merge sort 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def findMid(self, head):
        if(head is None or head.next is None):
            return head
        slow, fast = head, head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, head1, head2):
        if(head1 is None):
            return head2
        if(head2 is None):
            return head1
        current1 = head1
        current2 = head2
        dummyNode = Node(-1)
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
    def divide(self, head):
        if(head is None or head.next is None):
            return head 
        mid = self.findMid(head)
        left = mid.next
        right = head 
        mid.next = None
        
        left_halve = self.divide(left)
        right_halve = self.divide(right)
        
        return self.merge(left_halve, right_halve)
        