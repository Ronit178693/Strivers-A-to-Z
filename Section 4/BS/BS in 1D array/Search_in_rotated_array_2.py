# Brute Force
def search(nums:list, k:int):
    n = len(nums)
    for i in range(n):
        if(nums[i] == k):
            return True
    return False

'''
TC - O(N)
SC - O(1)
'''



# Optimal Solution
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while(low<=high):
            mid = (low+high)//2
            if(nums[mid] == target):
                return True
            # For the edge case where nums[low] == nums[mid] == nums[high] then we cant compare which half is sorted. One thing we know for sure is that mid is not our target therefore low and high wont be our targets too so me shift them by one place untile the condition fails
            if(nums[low] == nums[mid] and nums[mid] == nums[high]):
                low += 1
                high -= 1
                continue
            if(nums[low] <= nums[mid] and nums[mid] <= nums[high]): # In this case both the halves are sorted then we continuw with the normal BS
                if(nums[mid] > target):
                    high = mid - 1
                else:
                    low = mid + 1
            elif(nums[low] <= nums[mid]):
                if(nums[low]<=target<=nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if(nums[mid+1]<=target<=nums[high]):
                    low = mid+1
                else:
                    high = mid-1
        return False

'''
TC - O(N/2) in worst case when there are a lots of duplicants and we keep on shrinking 
TC - O(log n) in Avg. case
SC - O(1)
'''
