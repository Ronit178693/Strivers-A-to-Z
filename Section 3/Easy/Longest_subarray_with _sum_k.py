# Brute Force 

'''
Generate all the subarrays and find all the sub arrays with sum K then return the sub array with maximum length
'''

def Longest(arr:list, k:int):
    length = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum += arr[k]
            if(sum == k):
                length = max(length, j-i+1)
    return length              


'''
TC - O(N^3)
SC - O(1)
'''

# Better Solution

'''
The intution is that we dont have to compute the summition every time from scratch we can just add the new element to the old 
'''

def Longest(arr:list, k:int):
    length = 0
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if(sum == k):
                length = max(length, j-i+1)
    return length

'''
TC - O(N^2)
SC - 0(1)
'''



# Optimal Solution 
# 2 ponter approache used only if the array has +ves 
def longest(nums:list, k:int):
    i = 0
    sum = 0
    max_len = 0
    for j in range(len(nums)):
        sum += nums[j]
        
        while(sum>k and i<=j):
            sum -= nums[i]
            i += 1
        
        if(sum == k):
            max_len = max(max_len, j-i+1)
    return max_len
         
        
        
        
        
# Including negative elements
#  Brute Force
def longest(nums:list, k:int):
    max_len  = 0
    n = len(nums)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if(sum == k):
                max_len = max(max_len, j-i+1)
    return max_len

'''
TC - O(N^2)
SC - 0(1)
'''
def longest(nums:list, k:int):
    hash = {}
    pre_sum = 0
    max_len = 0
    for i in range(len(nums)):
        pre_sum += nums[i]
        if(pre_sum == k):
            max_len = max(max_len, i + 1)
        else:
            req = pre_sum - k
            if(req in hash):
                max_len = max(max_len, i - hash[req])
                
        if(pre_sum not in hash):
            hash[pre_sum] = i
    return max_len        

     
        
        
            
            
            
        