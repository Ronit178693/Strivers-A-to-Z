def NSE(nums):
    n = len(nums)
    # ans[i] = index of next strictly smaller element, or n if none
    ans, stack = [n] * n, []
    for i in range(n - 1, -1, -1):
        while(stack and nums[stack[-1]] > nums[i]):
            stack.pop()
        # If the stack is empty
        if(not stack):
            ans[i] = n
        # It hash elements
        else:
            ans[i] = stack[-1]
        stack.append(i)
    return ans
def PSE(nums):
    n = len(nums)
    # ans[i] = index of previous strictly smaller element, or -1 if none
    ans, stack = [-1] * n, []
    for i in range(n):
        while(stack and nums[stack[-1]] >= nums[i]):
            stack.pop()
        if(not stack):
            ans[i] = -1
        else:
            ans[i] = stack[-1]
        stack.append(i)
    return ans
def histograms(nums):
    area = 0
    nse = NSE(nums)
    pse = PSE(nums)
    for i in range(len(nums)):
        area = max(area, (nums[i]*(nse[i] - pse[i] - 1)))
    return area


# Optimal solution where we are going to find NSE and PSE in a single iteration 
# as we only have to make one pass we can calculate PSE while moving from left to right 
def histograms(nums):
    stack, area = [], 0
    for i in range(len(nums)):
        while(stack and nums[stack[-1]] >= nums[i]):
            element = stack.pop()
            nse = i
            if(len(stack) == 0):
                pse = -1
            else:
                pse = stack[-1]
            area = max(area, (nums[element] * (nse - pse - 1)))
        stack.append(i)
    # If there are lements left out in the stack, all those elements has no nse 
    if(stack):
        while(stack):
            element = stack.pop()
            nse = len(nums)
            if(len(stack) == 0):
                pse = -1
            else:
                pse = stack[-1]
            area = max(area, (nums[element] * (nse - pse - 1)))
    return area 
    
                        
            
            