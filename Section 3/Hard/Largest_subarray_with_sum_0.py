# Brute Force 
def Largest(nums:list, k:int = 0):
    n = len(nums)
    max_len = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if(sum == k):
                max_len = max(max_len, j-i+1)
    return max_len
'''
TC - O(N^2)
SC - O(1)
'''

# Optimal Solution 
def Largest(nums:list, k:int = 0):
    hash = {}
    n = len(nums)
    presum = 0
    max_len = 0
    for i in range(n):
        sum += nums[i]
        
        if(presum == k):
            max_len = max(max_len, i+1)
        else:
            req = presum - k
            if(req in hash):
                max_len = max(max_len, i - hash[req])
        
        if(presum not in hash):
            hash[presum] = i
    return max_len
        
