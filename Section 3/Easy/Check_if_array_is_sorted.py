def sorted(arr:list):
    is_sorted = True
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            is_sorted = False
            break
    return is_sorted
# TC = O(N)

# Leetcode 1752

#Brute Force Solution


def check(self, nums: list[int]) -> bool:
        # Initially we just have to check if the given list is sorted or not 
        sorted = True
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                sorted = False
                break
        if(sorted == True):
            return True
        else:
            rotation_position = 1
            new_nums = [0] * len(nums)
            while(sorted == False):
                if rotation_position >= len(nums):
                    return False

                for i in range(len(nums)):
                    new_nums[i] = nums[(i+rotation_position) % len(nums)]
                for i in range(len(new_nums)-1):
                    if(new_nums[i]>new_nums[i+1]):
                        rotation_position += 1
                        sorted = False
                        break
                    else:
                        sorted = True
            return sorted
        
'''
TC = O(N^2)
SC = O(N)
'''


# Instead of physically shifting the array positions and copying elements, we can solve this by looking at a core mathematical property of a rotated sorted array: It can have at most one "drop" point



# Optimized by AI 
def check(self, nums: list[int]) -> bool:
        drops = 0
        n = len(nums)
        
        for i in range(n):
            # (i + 1) % n smoothly checks the next element
            # and automatically compares the last element back to the first element
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
                
            # Early exit: If we find more than 1 drop, it's impossible
            if drops > 1:
                return False
                
        return True

            