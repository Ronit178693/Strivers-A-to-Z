'''
Celebrity = Known by all, but knows none 
'''


# Brut eForce solution using 2 arrays, 1) Known By and 2) I know 
def celebrity(nums):
    rows = len(nums)
    cols = len(nums[0])
    known_by = [0] * rows
    i_know = [0] * rows 
    for i in range(rows):
        for j in range(cols):
            # Someone knows someone
            if(nums[i][j] == 1):
                i_know[i] += 1
                known_by[j] += 1
            # If its a 0 we ignore it
    for i in range(len(known_by)):
        if(known_by[i] > rows - 1 and i_know[i] == 0):
            return i
    return -1


# There can me at lease 0 celebrities and at max 1 not more then 1 

def celebrity(nums):
    rows, cols = len(nums), len(nums[0]) 
    top, bottom = 0, rows - 1
    while(bottom > top):
        # If top knows bottom 
        if(nums[top][bottom] == 1):
            top += 1
        # if bottom knows top 
        elif(nums[bottom][top] == 1):
            bottom -= 1
        # both dont knows each other 
        else:
            top += 1
            bottom -= 1
    # We have probanly found our potential celebrity
    for i in range(rows):
            if(i == top):
                continue
                
            if(nums[top][i] == 0 and nums[i][top] == 1):
                continue
            else:
                return -1
    return top
                
