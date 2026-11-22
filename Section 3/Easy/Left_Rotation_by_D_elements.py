#  Brute Force Solution

arr = [int(x) for x in input("Enter the elements of the array separated by space: ").split(', ')]

def rotation(arr:list, d:int):
    n = len(arr)
    d = d % n  # To handle cases where d is greater than n
    temp = arr[:d]  # Store the first d elements in a temporary array
    for i in range(d, n):
        arr[i - d] = arr[i]  # Shift the remaining elements to the left
    arr[n - d:] = temp  # Place the stored elements at the end
    return arr

print("Original array:", arr)
d = int(input("Enter the number of positions to rotate left: "))
print("Array after left rotation by", d, "positions:", rotation(arr, d))

'''
TC - O(d){for comping the first d elements} + O(n-d){for shifting the remaining elements} + O(d){for placing the stored elements at the end} = O(n)
SC - O(d) as we are using a temporary array to store the first d elements
'''

# Easier Solution

def rotation(arr:list = [1, 2, 3, 4, 5, 6, 7], d:int = 3):
    n = len(arr)
    d = d % n  # To handle cases where d is greater than n
    arr[0:d] = arr[0:d][::-1]
    arr[d:n] = arr[d:n][::-1]
    arr[0:n] = arr[0:n][::-1]
    return arr
    
print("Array after left rotation by positions:", rotation())


# Optimized Solution

def rotation(arr:list = [1, 2, 3, 4, 5, 6, 7], d:int = 3):
    n = len(arr)
    d = d % n
    def reversal(l:int, r:int):
        while(l<r):
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r += 1
    reversal(0, d-1)
    reversal(d, n-1)
    reversal(0, n-1)
    return arr

print("Array after left rotation by positions:", rotation())

'''
TC - O(N)
SC - O(1)
'''



# Leetcode 189 

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
    #   If n is the length of the given list then performing n rotations brings the list to its original form so if we perform n+1 rotation of the list it is equivallent of performing only 1 rotation on the list

        n = len(nums)
        d = k % n # This gives the number of operations we have to perform 

        def reversal(l:int, r:int):
            while(l<r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        reversal(0, n-d-1)
        reversal(n-d, n-1)
        reversal(0, n-1)
        return nums
        


     
        