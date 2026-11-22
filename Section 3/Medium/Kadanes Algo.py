# Brute Force 

def Subarray(nums:list):
    max_sum = -float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            for k in range(i, j+1):
                sum += nums[k]
            if(sum > max_sum):
                max_sum = sum
    return max_sum

'''
TC - O(N^3)
SC - O(1)
'''

# Better Solution

def Subarray(nums:list):
    max_sum = -float('inf')
    for i in range(len(nums)):
         sum = 0
         for j in range(i, len(nums)):
            sum += nums[j]
            if(sum > max_sum):
                max_sum = sum
    return max_sum

'''
TC - O(N^2)
SC - O(1)
'''

# Optimized Solution
# Using Kadans Algo
def Subarray(nums:list):
    Max  = -float('inf')
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if(sum>Max):
            Max = sum
        if(sum<0):
            sum = 0
          
    return Max

'''
TC - O(N)
SC - O(1)
'''

                
            