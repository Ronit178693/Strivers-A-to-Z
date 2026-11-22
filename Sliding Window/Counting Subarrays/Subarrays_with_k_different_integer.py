# Brute Force Solution
'''
This is taking O(N^3) in TC as for every subarray we are converting it to its equivalent set
'''
def subarrays(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = set(nums[i : j + 1])
            if(len(subarray) == k):
                count += 1
            if(len(subarray) > k):
                break 
    return count 

# Better Solution
def subarrays(nums, k):
    count = 0
    for i in range(len(nums)):
        subarray = set()
        for j in range(i, len(nums)):
            subarray.add(nums[j])
            if(len(subarray) == k):
                count += 1
            if(len(subarray) > k):
                break 
    return count 

# Optimal Solution 
'''
Solve the problem for subarrays with different elements <= K and for <= K-1 then subtract them to get for K
'''
def subarryas(nums, k):
    l, r, count = 0, 0, 0
    hash = {}
    while(r < len(nums)):
        # If the number is not in hash
        if(nums[r] not in hash):
            hash[nums[r]] = 1
        # If the number is already in hash
        else:
            hash[nums[r]] += 1
        while(len(hash) > k):
            hash[nums[l]] -= 1
            if(hash[nums[l]] == 0):
                hash.pop(nums[l])
            l += 1
        count += r - l + 1
        r += 1
    return count 
            
            
        
    
    
    