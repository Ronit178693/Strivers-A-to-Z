#  Brute Force 

def helper(nums:list, distance:int, cows:int):
    cows_count = 1
    last_cow_position = nums[0]
    for i in range(1, len(nums)):
        if((nums[i] - last_cow_position) >= distance):
            cows_count += 1
            last_cow_position = nums[i]
        if(cows_count  == cows):
            return True
    return False
def Aggressive_cows(nums:list, cows:int):
    nums.sort()
    for distance in range(1, len(nums)):
        if(helper(nums, distance, cows) == True):
            continue
        else:
            return distance - 1
        
        
# Optimal Solution 

def helper 
        