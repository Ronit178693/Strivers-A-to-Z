# Brute Force solution 
def NGE2(nums):
    ans = []
    for i in range(len(nums)):
        
        for j in range(i, len(nums)):
            if(nums[j] > nums[i]):
                ans.append(nums[j])
                break
        else:
            for j in range(0, i):
                if(nums[j] > nums[i]):
                    ans.append(nums[j])
                    break 
            else:
                ans.append(-1)

    return ans 

# For the optimal solution hypothetally double the arrya 
'''
[2, 10, 12, 1, 11], 2, 10, 12, 1, 11
'''

def NGE2(nums):
    ans, stack = [], []
    # Traversing from the end of the duplicated array to the front
    for i in range(((2*len(nums)) - 1), -1, -1):
        # If there are already elements present in the satck and the elements present are less then the next element then pop those elements until the condition becomes true
        while(stack and nums[i%len(nums)] >= stack[-1]):
            stack.pop()
        # If we are now traversing through the original list instead of the duplicate 
        if(i < len(nums)):
            # If stack is empty
            if(not stack):
                ans.append(-1)
            else:
                ans.append(stack[-1])
        # If there are no elements in the stack just push an element in the stack
        stack.append(nums[i%len(nums)])
    ans.reverse()
    return ans
                                
            
        
