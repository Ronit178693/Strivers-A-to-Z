# Brute Force Solution 
def Search(nums:list, target:int):
    m_rows, n_columns = len(nums), len(nums[0])
    for rows in range(m_rows):
        for columns in range(n_columns):
            if(nums[rows][columns] == target):
                return True
    return False

'''
TC - O(m*n)
SC - O(1)
'''

# Better Soluution 
# Passing a row at a time in the BS helper function


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
TC - O(n + logm)
SC - O(1)
'''

# Optimal Solution 

def search(nums:list, target:int):
    m_rows, n_columns = len(nums), len(nums[0])
    row, column = 0, n_columns - 1
    while(row < m_rows and column >= 0):
        if(nums[row][column] == target):
            return True
        elif(nums[row][column] > target):
            column -= 1
        else:
            row += 1
    return False

'''
TC - O(n+m)
SC - O(1)
'''
