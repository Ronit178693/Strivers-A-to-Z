# Brute Force

def minimum(nums:list):
    n = len(nums)
    for i in range(n-1):
        # Finding the breaking point 
        if(nums[i] > nums[i+1]):
            # Returning the breaking point index which is the actual number of rotations
            return i + 1
        
'''
TC - O(N)
SC - O(1)
'''

# Optimal Solution
# Using BS 
def minimum(nums:list):
    low, high = 1, len(nums) - 1
    Min = float('inf')
    indx = -1
    while(low<=high):
        mid = (low+high)//2
        if(nums[low]<=nums[mid]):
            if(nums[low] < Min):
                indx = low
                Min = nums[low]
            low = mid + 1
        else:
            if(nums[mid] < Min):
                indx = mid
                Min = nums[mid]
            high = mid - 1
    return indx

'''
TC - O(logn)
SC - O(1)
'''

