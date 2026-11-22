# Brute Force solution using TC - O(max(headA, headB)) and SC - O(headA+headB)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def intersection(self, headA, headB):
        seen = set()
        while(headA is not None or headB is not None):
            if(headA is not None):
                if(headA not in seen):
                    seen.add(headA)
                    headA = headA.next
                else:
                    return headA
            if(headB is not None):
                if(headB not in seen):
                    seen.add(headB)
                    headB = headB.next
                else:
                    return headB
        return None

# Better Solution : By matching the length of both the linkedlists 
'''
Eliminated the time space complexity but the TC is O(len(l1)) + O(len(l2)) + O(difference) + O(min(len(l1), len(l2)))
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def length(self, head):
        count = 0
        current = head
        while(current is not None):
            count += 1
            current = current.next 
        return count
    def intersection(self, headA, headB):
        tempA, tempB = headA, headB
        lengthA, lengthB = self.length(headA), self.length(headB)
        if(lengthA > lengthB):
            difference = lengthA - lengthB
            for _ in range(difference):
                tempA = tempA.next
        else:
            difference = lengthB - lengthA
            for _ in range(difference):
                tempB = tempB.next
        while(tempA is not None and tempB is not None):
            if(tempA == tempB):
                return tempA
            tempA, tempB = tempA.next, tempB.next
        return None   
    
    
# Optimal Solution 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    
        