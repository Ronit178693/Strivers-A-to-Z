# Brute Force Solution
def Peak(nums:list):
    n = len(nums)
    for i in range(n - 1):
        if(nums[i] > nums[i+1]):
            return i
        
'''
TC - O(N)
SC - O(1)
'''



# Optimal Solution
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        n = len(nums)
        if(len(nums) == 1):
            return 0
        if(nums[0] > nums[1]):
            return 0
        if(nums[n-1] > nums[n-2]):
            return n-1
        
        low, high = 1, n-2
        
        while(low<=high):
            mid = (low+high)//2
            if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid
            if(nums[mid]<=nums[mid+1]):
                low = mid + 1
            elif(nums[mid]<=nums[mid-1]):
                high = mid - 1
'''
TC - O(logn)
SC - O(1)
'''


