# Brute Force Solution 
# Change the question to maximum subarray with atmost k 0's
#  TC - O(N^2) ans SC - O(1)
def ones(nums, k):
    n = len(nums)
    max_length = 0
    for i in range(n):
        count = k
        for j in range(i, n):
            if(count == 0 and nums[j] == 0):
                break
            if(nums[j] == 0 and count > 0):
                count -= 1
                max_length = max(max_length, j - i + 1)
            elif(nums[j] == 1):
                max_length = max(max_length, j - i + 1)
    return max_length

# Better Solution using Sliding window 
def ones(nums, k):
        l, r, max_length, zeros = 0, 0, 0, 0
        while(r < len(nums)):
            if(nums[r] == 1):
                max_length = max(max_length, r - l + 1)
                r += 1
            elif(nums[r] == 0):
                zeros += 1
                if(zeros > k):
                    while(zeros > k):
                        if(nums[l] == 0):
                            zeros -= 1
                        l += 1
                    max_length = max(max_length, r - l + 1)
                    r += 1
                elif(zeros <= k):
                    max_length = max(max_length, r - l + 1)
                    r += 1
        return max_length
    

# Optimal Solution 
def ones(nums, k):
        l, r, max_length, zeros = 0, 0, 0, 0
        while(r < len(nums)):
            if(nums[r] == 1):
                max_length = max(max_length, r - l + 1)
                r += 1
            else:
                zeros += 1
                if(zeros < k):
                    max_length = max(max_length, r - l + 1)
                    r += 1
                else:
                    if(nums[l] == 0):
                        zeros -= 1
                    l += 1
                    r += 1
        return max_length
    
            
                
                    
            
        
        
    
                
                
                
                
            
            
    