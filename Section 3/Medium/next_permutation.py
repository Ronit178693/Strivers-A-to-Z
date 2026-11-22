'''
For the Brute Force Solution:-
1)Generate all the permutations in an sorted order
2)Find for the input in that sorted array
3)Return the next element if present 

In interviews we must not code the brute force we should just give an overview with the time complexity 

if n is the length of the given array !n are the number of permutations so to find all the permutations we would need
arount o(!n*N) TC which is too high  
'''

# Optimized solution 

def permutation(nums:list):
    break_indx  = None

    for i in range(len(nums) - 1, 0, -1):
        if(nums[i] > nums[i-1]): # This finds the first break point in the array 
            break_indx = i-1
            break
    if(break_indx == None):
        nums.reverse()
        return nums
    for i in range(len(nums) - 1, break_indx, -1):
        if(nums[i] > nums[break_indx]):
            nums[i], nums[break_indx] = nums[break_indx], nums[i]
            break
            
    nums[break_indx+1 : len(nums)] = nums[break_indx+1 : len(nums)] [::-1]
    return nums

'''
TC - O(3N) - O(N)
SC - O(N)
'''

            
