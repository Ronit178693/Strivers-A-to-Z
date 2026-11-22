# Sol 1
class Solution:
    def searchInsert(self, nums: list[int], x: int) -> int:
          low, high = 0, len(nums) - 1
          ans = len(nums) # Considering there is no element which passes our condition of lower bound
          while(low<=high):
              mid = (low+high)//2
        # In the case where mid = x we will also have to check for the elements in the left half
        # if(nums[mid] == x):
        #     return mid
              if(nums[mid]>=x):
                  ans = mid
                  high = mid - 1
              else:
                  low = mid + 1
          return ans


#  If target exists in the array then we return it but if it dont we return the lower bound of the target


# Sol 2 
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
          low, high = 0, len(nums) - 1
          while(low <= high):
              mid = (low+high)//2
              if(nums[mid] == target):
                  return mid
              elif(nums[mid]>target):
                  high = mid - 1
              else:
                  low = mid + 1
          if(low>high):
            return low # Returning low instead of high because high is the last index element smaller then the target and low is the first index element greater then the target
