
# Better Solution
def missing(nums:list):
    n = len(nums)
    freq = [0] * (n + 1)
    for i in range(len(nums)):
        freq[nums[i]] += 1
    repeating = -1
    missing = -1
    for i in range(1, len(freq)):
        if(freq[i] > 1):
            repeating = 1
        if(freq[i] == 0):
            missing = 1
            
        if(repeating != -1 and missing != -1):
            break
    return [repeating, missing]
'''
TC - O(2N)
SC - O(N)
'''

# Optimal Solution using maths
def repeating(nums:list):
    n = len(nums)
    sum1 = 0
    sum2 = (n(n+1))//2
    s1 = 0
    s2 = (n*(n+1)(2*n+1 ))//6
    for i in range(n):
        sum1 += nums[i]
        s1 += nums[i]*nums[i]
        
    value1 = sum1 - sum2
    value2 = s1 - s2
    value2 = value2/value1
    x = (value1 + value2)//2
    y = x - value1
    return [x, y]
'''
TC - O(N)
SC - O(1)
'''


   
        
    
        
