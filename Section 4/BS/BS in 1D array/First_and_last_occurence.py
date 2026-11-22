# Brute Force 
def occurence(nums:list, k:int):
    n = len(nums)
    first = 0
    last = len(nums) - 1
    if(k in nums):
        while(nums[first] != k):
            first += 1
        while(nums[last] != k):
            last -= 1
        return [first, last]
    else:
        return [-1, -1]
        
    
'''
TC - O(3N)
SC - O(1)
'''

def lower_bound(self, nums:list[int], target:int):
        low, high = 0, len(nums) - 1
        lower = len(nums)
        while(low <= high):
            mid = (low+high)//2
            if(nums[mid]>=target):
                lower = mid
                high = mid - 1
            else:
                low = mid + 1
        return lower
def upper_bound(self, nums:list[int], target:int):
        low, high = 0, len(nums) - 1
        upper = len(nums)
        while(low <= high):
            mid = (low+high)//2
            if(nums[mid]>target):
                upper = mid
                high = mid - 1
            else:
                low = mid + 1
        return upper
def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self.lower_bound(nums, target)
        if(first == len(nums) or nums[first] != target):
            return [-1, -1]
        last = self.upper_bound(nums, target)
        return [first, last-1]

'''
TC - O(logn)
SC - O(1)
'''

            