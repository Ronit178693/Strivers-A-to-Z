# Brute Force Solution
 
'''
When forming a seperate matrix for answer we observe that 
[0][0] -> [0][3]  |  [1][0] -> [0][2]
[0][1] -> [1][3]  |  [1][1] -> [1][2]
[0][2] -> [2][3]  |  [1][2] -> [2][2]
[0][3] -> [3][3]  |  [1][3] -> [3][2]

we can observe that [i][j] = [j][n-i-1]
'''
def Rotate(matrix:list):
    n = len(matrix)
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for rows in range(n):
        for col in range(n):
            ans[col][n-rows-1] = matrix[rows][col]
    return ans  

'''
TC - O(N^2) + O(N^2) = O(2N^2) - O(N^2)
SC - O(N^2) - Using an external 2D Matrix 
'''

# Optimal Solution
'''
Transpose the given matrix and then reverse each row  
'''

def Rotation(matrix:list):
    n = len(matrix)
    # Finding the transpose of the given matrix
    for rows in range(n):
        for columns in range(rows+1, n):
            if(rows != columns):
                matrix[rows][columns], matrix[columns][rows] = matrix[columns][rows], matrix[rows][columns]
    for rows in range(n):
         matrix[rows].reverse()
            
'''
TC - O(2N^2) - O(N^2)
SC - O(1)
'''


