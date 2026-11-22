class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def merged(self, head1, head2):
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


    
                
                