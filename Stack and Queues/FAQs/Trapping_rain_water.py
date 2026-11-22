# Brute Force solution using TC - O(3N) and SC - O(2N)
def prefixMax(nums):
    pre_max = [nums[0]]
    for i in range(1, len(nums)):
        pre_max.append(max(nums[i], pre_max[i - 1]))
    return pre_max
def suffixMax(nums):
    suf_max = [nums[-1]] * len(nums)
    for i in range(len(nums) - 2,  -1, -1):
        suf_max[i] = max(nums[i], suf_max[i + 1])
    return suf_max
def rain_Water(nums):
    total = 0
    leftMax = prefixMax(nums)
    rightMax = suffixMax(nums)
    for i in range(len(nums)):
        # Condition to have water on top of it 
        if(nums[i] < leftMax[i] and nums[i] < rightMax[i]):
            total += min(leftMax[i], rightMax(i)) - nums[i]
    return total

