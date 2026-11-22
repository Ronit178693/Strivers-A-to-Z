# Brute Force solution using TC - O(N+left_nodes)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def leng(current):
        count = 0
        while(current is not None):
            count += 1
            current = current.next
        return count
    def remove(self, head, n):
        current = head
        length = self.leng(current)
        if(n == length):
            head = current.next
            current = None
            return head
        left_nodes = length-n
        i = 1
        while(i != left_nodes):
            current = current.next
            i += 1
        current.next = current.next.next
        return head
        