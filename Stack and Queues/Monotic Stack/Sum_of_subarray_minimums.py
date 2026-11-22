# Brute force solution 
'''
The brute force solution takes O(N^2) TC
'''

def subarrays(nums):
    sum = 0
    for i in range(len(nums)):
        mini = nums[i]
        for j in range(i, len(nums)):
            mini = min(mini, nums[j])
            sum += mini
    return (sum % ((10**9) + 7))

# Optimal solution 
'''
As we have to reduce the TC from O(N^2), we will try bringing it down to O(N) that is only single iteration 
'''
'''
Finding the contribution of element in the array and multiplying it with the element itself to find the total sum 
'''
'''
If there is no NSE then NSE = N
'' '' '' '' '' PSE then PSE = -1
'''

def NSE(nums):
    indx, stack = [-1] * len(nums), []
    # Traversing in reverse order in the list
    for i in range(len(nums) - 1, -1, -1):
        # When there are elements in the stack and the top of the stack is greater then the element we are on 
        while(stack and nums[stack[-1]] >= nums[i]):
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

def subarray(nums):
    MOD = (10**9) + 7
    hash_NSE = NSE(nums)
    hash_PSE = PSE(nums)
    total = 0
    for i in range(len(nums)):
        left = hash_NSE - i
        right = i - hash_PSE
        total += (left*right*nums[i])
    return total % MOD
        
            
    
