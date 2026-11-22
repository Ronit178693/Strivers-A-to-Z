# Brute Force solution using hashing 
'''
Usinf TC - O(N) and SC - O(N)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def length(self, head):
        seen = {}
        current = head
        temp = 0
        while(current is not None):
            if(current not in seen):
                temp += 1
                seen[current] = temp
                current = current.next
            if(current in seen):
                break
       
        length = temp - seen[current]
    
        return length

# Optomal Solution 
'''
Trying to eliiminate the extra space we were using 
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def length(self, head):
        slow, fast = head, head 
        count = 1
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if(fast == slow):
                break
        temp = slow
        while(temp.next != fast):
            count += 1
            temp = temp.next
        return count