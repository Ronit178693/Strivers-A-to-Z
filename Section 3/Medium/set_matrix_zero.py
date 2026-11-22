# Brute Force
def matrix(Matrix:list):
    rows = len(Matrix) #Total number of rows
    columns = len(Matrix[0]) # length of a column
    for i in range(rows):
        for j in range(columns):
            if(Matrix[i][j] == 0):
                # first turn the row to -1s 
                for col in range(columns):
                    if(Matrix[i][col] == 1):
                        Matrix[i][col] = -1
                for row in range(rows):
                    if(Matrix[row][j] == 1):
                        Matrix[row][j] = -1
    for i in range(rows):
        for j in range(columns):
            if(Matrix[i][j] == -1):
                Matrix[i][j] = 0
                
'''
TC - O((n*m) * (n+m) + (n*m))
SC - O(1)
'''

# Better Solution
def Matrix(matrix:list):
        rows_len = len(matrix) #Total number of rows
        columns_len = len(matrix[0]) # length of a column
        rows_count = [0] * columns_len
        columns_count = [0] * rows_len
        for rows in range(rows_len):
            for columns in range(columns_len):
                if(matrix[rows][columns] == 0):
                    rows_count[rows] = 1
                    columns_count[columns] = 1
                    
        for rows in range(rows_len):
            for columns in range(columns_len):
                if(rows_count[rows] == 1 or columns_count[columns] == 1):
                    matrix[rows][columns] = 0
                    
'''
TC - O((n*m) + (n*m)) - O(nm)
SC - O(m + n)
'''



   
        
        
                
                    
            
            
        