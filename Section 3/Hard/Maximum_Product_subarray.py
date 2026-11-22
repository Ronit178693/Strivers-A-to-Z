# Optimal Solution
def product(nums:list):
    Max = float('-inf')
    prefix = 1
    suffix = 1
    for i in range(len(nums)):
        if(prefix == 0):
            prefix = 1
        if(suffix == 0):
            suffix = 1
        prefix = prefix * nums[i]
        suffix = suffix * nums[len(nums) - i - 1]
        Max = max(Max, prefix, suffix)
    return Max
'''
TC - O(N)
SC - O(1)
'''




        

    
    