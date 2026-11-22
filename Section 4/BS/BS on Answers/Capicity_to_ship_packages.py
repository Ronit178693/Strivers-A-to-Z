#  Brute Force 
def days_required(nums:list, cap:int):
    days = 1
    sum = 0
    for i in range(len(nums)):
        if(sum + nums[i] > cap):
            days += 1
            sum = nums[i]
        else:
            sum += nums[i]
    return days

def ship(nums:list, d:int):
    Min = max(nums)
    Max = 0
    for i in nums:
        Max += i
    for cap in range(Min, Max+1):
        # Returns the minimum capicity of the ship we need 
        if(days_required(nums, cap) <= d):
            return cap
        
# Optimal Solution

def days_required(nums:list, cap:int):
    days = 1
    load = 0
    for i in range(len(nums)):
        if(load+nums[i] > cap):
            days += 1
            load = nums[i]
        else:
            load += nums[i]
    return days 
def ship(nums:list, d:int):
    Min = max(nums)
    Max = sum(nums)
    while(Min<Max):
        cap = (Min+Max)//2
        if(days_required(nums, cap)<=d):
            high = cap
        else:
            low = cap + 1
    return Min