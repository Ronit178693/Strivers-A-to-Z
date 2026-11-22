# Brute Force 

def Largest(nums:list, k:int = 0):
    n = len(nums)
    count = 0
    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor  = xor ^ nums[j]
            if(xor == k):
                count += 1
    return count

# Optimal Solution
def Largest(nums:int, k:int):
    hash = {}
    n = len(nums)
    count = 0
    xor = 0
    hash[xor] = 1
    for i in range(n): 
        xor = xor ^ nums[i]
        req = xor ^ k
        if(req in hash):
            count += hash[req]
        hash[xor] = hash.get(xor, 0) + 1
    return count