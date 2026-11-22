# Brute Force Solution 
def subarrays(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        temp = 0
        for j in range(i, n):
            # If the number is odd 
            if(nums[j] % 2 == 1):
                temp += 1
            if(temp == k):
                count += 1
            if(temp > k):
                break
    return count 

# Optimal Solution 
'''
TC - O(2N) as we are making 2 passes in the array
SC - O(1)
'''

def solution(nums, k):
    def subarrays(nums, k):
        r, l, count, odds = 0, 0, 0, 0
        while(r < len(nums)):
            if(nums[r] % 2 == 1):
                odd += 1
            while(odd > k):
                if(nums[l] % 2 == 1):
                    odd -= 1
                l += 1
            count += r - l + 1
            r += 1
        return count 
    return subarrays(nums, k) - subarrays(nums, k - 1)
        
             
            