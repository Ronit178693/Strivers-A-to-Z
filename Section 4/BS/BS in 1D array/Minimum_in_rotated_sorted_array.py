# Brute Force
def minimum(nums:list):
    n = len(nums)
    min = float('inf')
    for i in range(n):
        if(nums[i]<min):
            min = min(min, nums[i])
    return min
'''
TC - O(N)
SC - O(1)
'''

# Optimal Solution 1
class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        Min = float('inf')
        while(low<=high):
            mid = (low+high)//2
            Min = min(Min, nums[mid])
            # The array is sorted 
            if(nums[low]<=nums[mid]<=nums[high]):
                high = mid - 1
            # The left half is sorted then we move to the right half
            elif(nums[low]<=nums[mid]):
                low = mid + 1
            # If the right half is sorted we move to the left half 
            else:
                high = mid - 1
        return Min
    
# Optimal Solution 2

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        Min = float('inf')
        while(low<=high):
            mid = (low+high)//2
            # The left half is sorted 
            if(nums[low]<=nums[mid]):
                Min = min(Min, nums[low])
                low = mid + 1
            else:
                Min = min(Min, nums[mid])
                high = mid - 1
        return Min
