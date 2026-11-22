# Brute Force
def count(nums:list, k:int):
    n = len(nums)
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if(sum == k):
                count += 1
    return count

# Optimized Solution
# Using Pre Sum

def count(nums:list, k:int):
    n = len(nums)
    presum = 0
    hash = {}
    hash[presum] = 1
    count = 0
    for i in range(n):
        presum += nums[i]
        req = presum - k
        if(req in hash):
            count += hash[req]
        hash[presum] = hash.get(presum, 0) + 1
    return count

''''
TC - O(N)
SC - O(N)
'''
        