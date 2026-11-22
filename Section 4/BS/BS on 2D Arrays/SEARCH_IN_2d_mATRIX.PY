#  Brute Force 
def search(nums:list, target:int):
    m_rows = len(nums)
    n_columns = len(nums[0])
    for rows in range(m_rows):
        for columns in range(n_columns):
            if(nums[rows][columns] == target):
                return True
    return False 
'''
TC - O(m*n)
SC - O(1)
'''

#  Better Solution
def BS(row:list, target:int):
    low, high = 0, len(row) - 1
    while(low<=high):
        mid = (low+high)//2
        if(row[mid] == target):
            return True
        elif(row[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    return False

def search(nums:list, target:int):
    m_rows, n_columns = len(nums), len(nums[0])
    for rows in range(m_rows):
        if(nums[rows][0]<= target<=nums[rows][n_columns-1]):
            return BS(nums[rows], target)
    return False
'''
TC - O(n+logm)
SC - O(1)
'''

# Optimal Solution 
    
def BS(nums:list, target:int):
    m_rows, n_columns = len(nums), len(nums[0])
    low, high = 0, (m_rows*n_columns) - 1
    while(low<=high):
        mid = (low+high)//2
        column_cord, row_cord = mid % n_columns, mid // n_columns
        if(nums[row_cord][column_cord] == target):
            return True
        elif(nums[row_cord][column_cord] > target):
            high = mid - 1
        else:
            low = mid + 1
    return False


'''
TC - O(log(m*n))
SC - O(1)
'''

            