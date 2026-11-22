#  Brute Force 
def rotated(nums:list, k:int):
    n = len(nums)
    for i in range(n):
        if(nums[i] == k):
            return i
    return -1

'''
TC - O(N)
SC - O(1)
'''

# Optimal Solution

def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while(low<=high):
            mid = (low+high)//2
            if(nums[mid] == target):
                return mid
                # If left half is sorted 
            if(nums[low] <= nums[mid]):
                # First we will check if the targest lies in the left half if it lies in the left half we continues with it if not then we move on the the right half
                if(nums[low] <= target and target <=nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if(nums[mid] <= target and nums[high] >= target):
                    low = mid+1
                else:
                    high = mid - 1
        return -1
