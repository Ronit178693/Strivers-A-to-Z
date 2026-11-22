#  Brute Force Solution

def remove_duplicates(arr:list):
      array = set(arr)  # Using set to remove duplicates
      return list(sorted(array))  # Converting set back to list and sorting it
    
'''
TC = O(n + klogk) where n is the length of the array and k is the number of unique elements in the array
SC = O(k) where k is the number of unique elements in the array
'''

# Optimal Solution 

def remove_duplicate(arr:list):
    i, j = 0, 1
    while(j<len(arr) and i<len(arr)):
        if(arr[i] == arr[j]):
            j += 1
        else:
            arr[i+1] = arr[j]
            i+=1
    return arr[0:i+1]
print(remove_duplicate([1, 1, 2, 2, 3, 4, 4, 5]))

'''
TC = O(N)
SC = O(N) - As we are slicing the array to return only the unique elements, it takes O(N) space in the worst case when all elements are unique.
'''


# Leetcode 26

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i, j = 0, 1
        while(i<len(nums) and j<len(nums)):
            if(nums[i]==nums[j]):
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
        
        return i+1

'''
TC = O(N)
SC = O(1) - In Place solution, we are not using any extra space, we are just modifying the input array. 
'''
        

