# Brute Focre 
'''
Generate all the pairs which meets the requirement and increment the counter by 1 each time you find a pair

TC - O(N^2)
SC - O(1)
'''

# Optimal Solution Using Merge Sort 

def merge(nums:list, low:int, mid:int, high:int):
    left , right= low, mid+1
    temp = []
    count = 0
    while(left<=mid and right<=high):
        if(nums[left] > nums[right]):
            temp.append(right)
            count = mid-left+1
            right += 1
        else:
            temp.append(left)
            left += 1
    while(left <= mid):
        temp.append(left)
        left += 1
    while(right <= high):
        temp.append(right)
        right += 1
        
    for i in range(len(temp)):
        nums[i] = temp[i]
    
def merge_sort(nums:list, high:int, low:int):
    if(low>=high):
        return 
            
   
    
