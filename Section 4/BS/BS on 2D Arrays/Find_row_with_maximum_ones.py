'''
The 2D array on;ly contains of 1, 0 and each row in the arrya is sorted 

Approache 1
Go through each row and count the number of 1's in each row store the row with maximum number of 1's in a variable and then return the row with maximum number of 1's
'''

#  Brute Force 

def traversal(nums:list):
    n_rows = len(nums)
    m_columns = len(nums[0])
    row_with_max_ones = -1
    ones = 0
    for rows in range(n_rows):
        count = 0
        for columns in range(m_columns):
            if(nums[rows][columns] == 1):
                count += 1
        if(count > ones):
            ones = count
            row_with_max_ones = rows
    return row_with_max_ones

'''
TC - O(m*n)
SC - O(1)
'''

'''
The complexit of the brute solution is already m*n and the rows are sorted so we cna get intuted that BS might be applicable 

In BS on 2D arrays we cannot optimize the row traversal so we will optimize the column traversal using BS and we will get the first occurence of 1 in each row and then we will get the row with maximum number of 1's
'''

#  Optimal Solution 

def lower_bound(nums:list, target:int):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] >= target):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
def traversal(nums:list):
    n_rows = len(nums)
    m_columns = len(nums[0])
    ones = 0
    row_with_max_ones = -1
    for rows in range(n_rows):
        index_first_one = lower_bound(nums[rows], 1)
        number_of_ones = m_columns - index_first_one
        if(number_of_ones > ones):
            ones = number_of_ones
            row_with_max_ones = rows
    return row_with_max_ones

'''
TC - O(n*log m)
SC - O(1)
'''



            
