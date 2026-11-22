# The stack here will be monotonically decreasin
def NSE(nums):
    ans, stack = [-1] * len(nums), []
    # Traversing in reverse order in the list
    for i in range(len(nums) - 1, -1, -1):
        # When there are elements in the stack and the top of the stack is greater then the element we are on 
        while(stack and stack[-1] >= nums[i]):
            stack.pop()
        # If the stack goes empty then there was no element smaller then the elemnt we are on 
        if(not stack):
            ans[i] = -1
        # If the while loop does not hits this means we dont have any issue and the top is the smallest element for the current element 
        else:
            ans[i] = stack[-1]
        stack.append(nums[i])
    return ans 
            
             
            