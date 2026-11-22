# Brute Force Solution 
def binary(nums, goal):
    count = 0
    n = len(nums)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if(sum == goal):
                count += 1
            elif(sum > goal):
                break
    return count 
            
# Optimal Solution 
def answer(nums, goal):
    # Subarrays with sum <= goal
    def binary(nums, goal):
        if(goal < 0):
            return 0
        l, r, sum, count = 0, 0, 0, 0
        while(r < len(nums)):
            sum += nums[r]
            while(sum > goal):
                sum -= nums[l]
                l += 1
            count += r - l + 1
            r += 1
        return count 
    return binary(nums, goal) - binary(nums, goal - 1)
        