'''
Problems Related to pascal triangle:-

1) Given the row and the column number find the element there - SOlution:
row - 1 C column - 1 = exact element
2) Print nth row of the pascle triangle 
3) Print the entire pascle triangle 
'''
# Code for problem 1 
def problem_1(row:int, column:int):
    res = 1
    for i in range(column - 1):
        res = res * ((row - 1)- i)
        res = res//(i+1)
    return res 

'''
TC - O(c)
SC - O(1)
'''

# Problem 2
# Brute Force Solution
def problem_2( row:int):
    # Nth row have n number of columns 
    ans = []
    for i in range(1, row+1):
        res = 1
        for j in range(i - 1):
            res = res *((row - 1) - j)
            res = res // (j + 1)
        ans.append(res)
    return ans
 
'''
TC - O(N*C)
SC - O(r)
'''

# Optimal Solution
def Problem_2(row:int):
    ans = []
    res = 1
    ans.append(res)
    for col in range(1, row):
        res = res *(row - col)
        res = res // (col)
        ans.append(res)
    return ans

'''
TC - O(r)
SC - O(c)
'''

# Problem 3

# Brute Force 

def value(row:int, column:int):
        res = 1
        for i in range(column - 1):
            res = res *((row - 1) - i)
            res = res//(i+1)
            
def triangle(rows:int):
    triangle = []
    for i in range(1, rows+1):
        ans = []
        value()
    
# Optimal Solution


def triangle(rows:int):
    triangle = []
    for row in range(1, rows + 1):
        ans = []
        res = 1
        ans.append(res)
        for col in range(1, row):
            res = res * (row - col);
            res = res/(col)
            ans.append(res)
        triangle.append(ans)
    return triangle   

'''
TC - O(R^2)
SC - O(2R)
'''




        
        
  
