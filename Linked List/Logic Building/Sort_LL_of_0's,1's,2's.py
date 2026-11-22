# Brute Force solution 
'''
Keeping a count of 1's, 2's and 0's in the linkedlist then rewriting the linkedlist 
using O(2N) TC and O(1) SC 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LL:
    def sort(self, head):
        current = head 
        count_0, count_1, count_2 = 0, 0, 0
        while(current is not None):
            if(current.data == 0):
                count_0 += 1
            elif(current.data == 1):
                count_1 += 1
            else:
                count_2 += 1
            current = current.next
        # Once we have all the count values we rewrite the current linkedlist 
        current_new = head
        while(current_new is not None):
            if(count_0 != 0):
                current_new.data = 0
                count_0 -= 1
            elif(count_1 != 0):
                current_new.data = 1
                count_1 -= 1
            else:
                current_new.data = 2
                count_2 -= 1
            current_new = current_new.next
        return head
    
    
# Optimal Solution without using O(2N) TC 

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class LL:
    def sort(self, head):
        # To cut down on TC we will update the links 
         # Create dummy headers for tracking three separate lists
        dummyNode_0 = ListNode()
        dummyNode_1 = ListNode()
        dummyNode_2 = ListNode()
        
        # Travelers to dynamically build out each group list
        temp_0 = dummyNode_0
        temp_1 = dummyNode_1
        temp_2 = dummyNode_2
        
        current = head 
        
        while(current is not None):
            if(current.data == 0):
                temp_0.next = current
                temp_0 = temp_0.next
            elif(current.data == 1):
                temp_1.next = current
                temp_1 = temp_1.next
            else:
                temp_2.next = current
                temp_2 = temp_2.next
            current = current.next
        dummy_head_0 = dummyNode_0.next
        dummy_head_1 = dummyNode_1.next
        dummy_head_2 = dummyNode_2.next
        
        temp_0.next = dummy_head_1
        temp_1.next = dummy_head_2
        temp_2.next = None
        return dummy_head_0
        


