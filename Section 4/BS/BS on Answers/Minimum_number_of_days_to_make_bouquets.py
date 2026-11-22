# Brute Force
def Helper(nums:list, days:int, k:int):
    bouquets = 0
    blooms = 0
    i = 0
    while(i<=len(nums) - 1):
        if(nums[i] <= days):
            blooms += 1
            i += 1
        else:
            blooms = 0
            i += 1
        if(blooms == k):
            bouquets += 1
            blooms = 0
    return bouquets

        
         
def Minimum(nums:list, m:int, k:int):
    Min, Max = min(nums), max(nums)
    for days in range(Min, Max+1):
        if(Helper(nums, days, k) >= m):
            return days
    return -1   


# Optimal Solution 

def Helper(nums:list, days:int, k:int):
    bouquets = 0
    blooms = 0
    i = 0
    while(i<=len(nums) - 1):
        if(nums[i] <= days):
            blooms += 1
            i += 1
        else:
            blooms = 0
            i += 1
        if(blooms == k):
            bouquets += 1
            blooms = 0
    return bouquets

def Minimum(nums:list, m:int, k:int):
    Min, Max = min(nums), max(nums)
    Min_days = float('inf')
    while(Min<=Max):
        day = (Min+Max)//2
        if(Helper(nums, day, k) >= m):
            Min_days = min(Min_days, day)
            Max = day - 1
        else:
            Min = day + 1
    if(Min_days == float('inf')):
        return -1
    else:
        return Min_days
            
            

        
  