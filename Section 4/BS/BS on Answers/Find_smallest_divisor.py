import math
# Brute Force 

def calculation(nums:list, divisor:int):
    sum = 0
    for i in nums:
        result = math.ceil(i/divisor)
        sum += result
    return sum
        
def divisors(nums:list, threshold:int):
    Min, Max = 1, max(nums)
    for divisor in range(Min, Max + 1):
        if(calculation(nums, divisor) <= threshold):
            return divisor 
        
        
# Optimal Solution
def calculation(nums:list, divisor:int):
    sum = 0
    for i in nums:
        result = math.ceil(i/divisor)
        sum += result
    return sum
def divisors(nums:list, threshold:int):
    Min, Max = 1, max(nums)
    ans = float('inf')
    while(Min <= Max):
        divisor = (Min+Max)//2
        if(calculation(nums, divisor) <= threshold):
            ans = min(ans, divisor)
            Max = divisor - 1 
        else:
            Min = divisor + 1
    return ans
            
   
        
        
    