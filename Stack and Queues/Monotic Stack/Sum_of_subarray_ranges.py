# Brute Force SOlution 
def subarray_range(nums):
    sum = 0
    for i in range(len(nums)):
        mini, maxi = nums[i], nums[i]
        for j in range(i, len(nums)):
            mini, maxi = min(mini, nums[j]), max(maxi, nums[j])
            sum += (maxi - mini)
    return sum

# Optimal Solution 

def NSE(nums):
    indx, stack = [-1] * len(nums), []
    # Traversing in reverse order in the list
    for i in range(len(nums) - 1, -1, -1):
        # When there are elements in the stack and the top of the stack is greater then the element we are on 
        while(stack and nums[stack[-1]] > nums[i]):
            stack.pop()
        # If the stack goes empty then there was no element smaller then the elemnt we are on 
        if(not stack):
            indx[i] = len(nums)
        # If the while loop does not hits this means we dont have any issue and the top is the smallest element for the current element 
        else:
            indx[i]= stack[-1]
        stack.append(i)
    return indx

def PSE(nums):
    indx, stack = [-1] * len(nums), []
    for i in range(len(nums)):
        while(stack and nums[i] <= nums[stack[-1]]):
            stack.pop()
        if(not stack):
            indx[i] = -1
         # If the while loop does not hits this means wdont have any issue and the top is the smalleselement for the current element 
        else:
            indx[i] = stack[-1]
        stack.append(i)
    return indx

def NGE(nums):
    n = len(nums)
    indx, stack = [-1] * n, []
    for i in range(len(nums) - 1, -1, -1):
        while(stack and nums[i] > nums[stack[-1]]):
            stack.pop()
        if(not stack):
            indx[i] = n
        else:
            indx[i] = stack[-1]
        stack.append(i)
    return indx

def PGE(nums):
    n = len(nums)
    indx, stack = [-1] * n, []
    for i in range(len(nums)):
        while(stack and nums[i] >= nums[stack[-1]]):
            stack.pop()
        if(not stack):
            indx[i] = -1
        else:
            indx[i] = stack[-1]
        stack.append(i)
    return indx

def subarray_min(nums):
    hash_NSE = NSE(nums)
    hash_PSE = PSE(nums)
    total = 0
    for i in range(len(nums)):
        left = hash_NSE[i] - i
        right = i - hash_PSE[i]
        total += (left*right*nums[i])
    return total 

def subarray_max(nums):
    hash_NSE = NGE(nums)
    hash_PSE = PGE(nums)
    total = 0
    for i in range(len(nums)):
        left = hash_NSE[i] - i
        right = i - hash_PSE[i]
        total += (left*right*nums[i])
    return total 

def subarray_range(nums):
    return subarray_max(nums) - subarray_min(nums)
