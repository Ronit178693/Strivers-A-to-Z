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

def rectangle(nums):
    max_area = 0
    heights = [0] * len(nums[0])
    # Looping through the rows 
    for rows in range(len(nums)):
        # Looping through the columns 
        for cols in range(len(nums[0])):
            if(nums[rows][cols] == '1'):
                heights[cols] += 1
            # If the element is 0
            else:
                heights[cols] = 0
        max_area = max(max_area, histograms(heights))
    return max_area
                
            
            
        
        
        