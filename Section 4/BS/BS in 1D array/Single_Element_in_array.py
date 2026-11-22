# Brute Force Solution
# Use Hashing


# Better Solution 
def Single(nums:list):
    n = len(nums)
    if(n == 1):
        return nums[0]
    for i in range(0, n-1, 2):
        if(nums[i] != nums[i+1]):
            return nums[i]
'''
TC - O(N)
SC - O(1)
'''

# Optimal Solution
'''
before the single element duplicants will be in the pair of (even, odd) but after the single element
duplicants will be in the pair of (odd, even)
'''
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
         n = len(nums)
         low, high = 0, n - 1
         if(n == 1):
             return nums[0]
         if(nums[low] != nums[low+1]):
             return nums[low]
         if(nums[high] != nums[high-1]):
             return nums[high]
         low, high = low+1, high-1
         while(low<=high):
            mid = (low+high)//2
            if(nums[mid] != nums[mid-1] and nums[mid] !=nums[mid+1]):
                return nums[mid]
    #    If mid is on odd index then it should have a duplicant on mid - 1 even index
            if(mid%2 == 1 and nums[mid] == nums[mid-1] or mid%2 == 0 and nums[mid] == nums[mid+1]):
                low = mid+1
            elif(mid%2 == 0 and nums[mid] == nums[mid-1] or mid%2 == 1 and nums[mid] == nums[mid+1]):
                high = mid - 1
                
'''
TC - O(logn)
SC - O(1)
'''

            
       
   