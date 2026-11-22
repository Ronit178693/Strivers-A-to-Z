# Brute Force 
def Consecutive(nums:list)->int:
    n = len(nums)
    largest = 1
    for i in range(n):
        x = nums[i]
        count = 1
        while(x+1 in nums):
            count += 1
            x = x+1
            if(count > largest):
                largest = count
    return largest

'''
TC - O(N^3)
SC - O(1)
'''

# Optimized Solution
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        longest = 1
        seen = set(nums)
        
        # CORRECT WAY: Loop through the elements inside the set directly
        for num in seen:
            # Check if 'num' is the starting number of a sequence
            if num - 1 not in seen:
                x = num
                count = 1
                
                # Check for consecutive numbers ahead
                while x + 1 in seen:
                    x = x + 1  # Advance our sequence tracker
                    count += 1
                    
                longest = max(count, longest)
                
        return longest

