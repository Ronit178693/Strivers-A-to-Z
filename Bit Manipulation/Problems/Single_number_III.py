# Brute Force solution using hashing 

# Optimal Solution using the concept of buckets 
'''
As it is clearly stated that there are only 2 elements appearing once and rest elements appear exactly 2 times.

as the two elements appearing once will always be distinct having atleast one bit mismatching so they will always lye is different buckets and rest of the elements will lye in their respective buckets in pairs
'''

def singleNumber(self, nums: list[int]) -> list[int]:
    xor = 0
    for i in range(len(nums)):
        xor = xor ^ nums[i]
    right_most_bit = (xor ^ (xor - 1)) & xor
    buck1, buck2 = 0, 0
    for i in range(len(nums)):
        if(nums[i] & right_most_bit != 0):
            buck1 = buck1 ^ nums[i]
        else:
          buck2 = buck2 ^ nums[i]
    return [buck1, buck2]  
