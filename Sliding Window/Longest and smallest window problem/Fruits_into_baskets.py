# Brute Force SOlution generating all the subarrays 
# This solution uses TC - O(N^2) and SC - O(2)
def fruits(nums):
    max_count = 0
    for i in range(len(nums)):
        hash = set()
        for j in range(i, len(nums)):
            if(nums[j] not in hash and len(hash) < 2):
                hash.add(nums[j])
                max_count = max(max_count, j - i + 1)
            elif(nums[j] in hash):
                max_count = max(max_count, j -i + 1)
            else:
                break
    return max_count

# Better Solution 

def fruits(nums):
    l, r, max_length, hash = 0, 0, 0, {}
    while(r < len(nums)):
        if(nums[r] not in hash):
            hash[nums[r]] == 1
            if(len(hash) < 2):
                max_lenght = max(max_length, r - l + 1)
                r += 1
        elif(nums[r] in hash):
            hash[nums[r]] += 1
            max_lenght = max(max_length, r - l + 1)
            r += 1
        else:
            # When the length of the hash increases 
            while(len(hash) > 2):
                if(hash[nums[l]] == 0):
                    hash.pop(nums[l])
                    l += 1
                    max_lenght = max(max_length, r - l + 1)
                else:
                    hash[nums[l]] -= 1
                    l += 1
    return max_length

            
            
            
            
            
            
        
                    
            
            
        
        
        