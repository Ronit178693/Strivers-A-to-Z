def points(nums, k):
    Max_points = 0
    left_sum = 0
    for i in range(k):
        left_sum += nums[i]
        Max_points = left_sum
    right_sum = 0
    right_indx = len(nums) - 1
    for i in range(k - 1, -1, -1):
        left_sum -= nums[i]
        right_sum += nums[right_indx]
        right_indx -= 1
        total = left_sum + right_sum
        Max_points = max(Max_points, total)
    return Max_points
        
        