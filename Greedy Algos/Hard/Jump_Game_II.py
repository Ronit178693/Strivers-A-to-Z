# Given we will always reach the end 
# Brute Force Solution
# This Solution is taking exponential time
def jump_game(nums):
    def generate(nums, count, i):
        min_count = float('inf')
        if(i >= len(nums) - 1):
            return count
        for j in range(1, nums[i] + 1):
            min_count = min(min_count, generate(nums, count + 1, i + j))
        return min_count 
    return generate(nums, 0, 0)

# Optimal Solution 
def jump_game(nums):
    l, r, jump = 0, 0, 0
    while(r < len(nums)):
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(i + nums[i], farthest)
        l = r + 1
        r = farthest
        jump += 1
    return jump     
        

    
            
        
        