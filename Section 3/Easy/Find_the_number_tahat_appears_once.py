# Brute Force 

def find(arr:list):
    
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if(arr[j] == arr[i]):
                count += 1
        if(count == 1):
            return i
        
print(find(arr))
                    

'''
TC - O(N^2)
SC = O(1)
'''

# Better Solution
# Using Hashing

def find(arr:list):
    max = arr[0]
    for i in range(len(arr)-1):
        if(arr[i]<arr[i+1]):
            max = arr[i+1]
    freq = [0] * max+1
    for j in range(len(arr)):
        freq[arr[j]] += 1
    for k in range(len(freq)):
        if(freq[k] == 1):
            return k
'''
TC - O(3N)
SC - O[N]
'''

# Optimal Solution
# Leetcode 136

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # XOR of an element with the same element returns 0, eg. 3^3 = 0 so the intution is if every number appears twice then only one number appears once then the XOR of all the elements in the array must be equal to the number that appears once 

        XOR = 0
        for i in range(len(nums)):
            XOR = XOR ^ nums[i] #Starting with 0^nums[i] = arr[i]{property} then from next iteration we get arr[i]^arr[i+1]
        return XOR
    
'''
TC - O(N)
SC - O(1)
'''
