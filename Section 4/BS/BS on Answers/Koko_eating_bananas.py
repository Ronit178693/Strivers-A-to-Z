import math

# Better Solution


def Maximum(nums:list):
    Max = nums[0]
    for i in range(len(nums) - 1) :
        if(nums[i] < nums[i+1]):
            Max = max(Max, nums[i+1])
    return Max
def Checker(nums:list, k:int):
    hours = 0
    i = 0
    piles = nums.copy()
    while(i <= len(piles) - 1):
        if(piles[i] <= k):
            hours += 1
            i += 1
        else:
            hours += 1
            piles[i] = piles[i] - k
            if(piles[i] == 0):
                i += 1 
    return hours  
def Koko(nums:list, h:int):
    Min, Max = 1, Maximum(nums)
    Min_k = 1
    while(Min<=Max):
        mid = (Min+Max)//2
        if(Checker(nums, mid) > h):
            Min = mid + 1
        else:
            Min_k = mid
            Max = mid - 1
    return Min_k

# Optimal Solution

def Maximum(nums:list):
    Max = nums[0]
    for i in range(len(nums) - 1) :
        if(nums[i] < nums[i+1]):
            Max = max(Max, nums[i+1])
    return Max
def Checker(nums:list, k:int):
    hours = 0
    for i in nums:
        hours += math.ceil(i/k)
    return hours
def Koko(nums:list, h:int):
    Min, Max = 1, Maximum(nums)
    Min_k = 1
    while(Min<=Max):
        mid = (Min+Max)//2
        if(Checker(nums, mid) > h):
            Min = mid + 1
        else:
            Min_k = mid
            Max = mid - 1
    return Min_k
            
            