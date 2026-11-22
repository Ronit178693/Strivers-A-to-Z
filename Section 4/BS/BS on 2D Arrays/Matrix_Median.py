'''
Given that the matrix is sorted row wise and the number of elements in the matrix are always odd
'''
# Median is only found when the array is sorted 

# Brute Force
def Median(nums:list):
    m_rows, n_columns = len(nums), len(nums[0])
    arr = []
    for i in range(m_rows):
        for j in range(n_columns):
            arr.append(nums[i][j])
    arr.sort()
    return arr[len(arr)//2] 

#  Optimal Solution 
