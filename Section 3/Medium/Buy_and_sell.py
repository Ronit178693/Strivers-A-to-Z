# Brute Force 
def stocks(nums:list):
    # i = selling day
    # j = Potential buying day
    max_profit = 0
    for i in range(1, len(nums)):
        profit = 0
        for j in range(0, i):
            profit = nums[i] - nums[j]
            if(profit > max_profit):
                max_profit = profit
    return max_profit

'''
TC - O(N^2)
SC - O(1)
'''


# Optimized Solution

def stocks(nums:list):
    min = nums[0]
    max_profit = 0
    for i in range(1, len(nums)):
        cost = nums[i] - min 
        if(cost > max_profit):
            max_profit = cost
        if(min > nums[i]):
            min = nums[i]
    return max_profit

'''
TC - O(N)
SC - O(1)
'''
              
                
            