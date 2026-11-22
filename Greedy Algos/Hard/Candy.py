'''
If child A and child B have the same rating, child B does not need to inherit or continue child A's streak. Child B's left-side requirement resets to the baseline minimum: 1 candy.
'''
# Brute Force 

def candy(ratings):
    # As no matter what is the ratting of the first children we will always give him 1 candy as we are trying to be greedy, checking only the left neighbours first
    left = [1]
    count_left = 1
    for i in range(1, len(ratings)):
        if(ratings[i - 1] < ratings[i]):
            count_left += 1
            left.append(count_left)
        elif(ratings[i - 1] >= ratings[i]):
            count_left = 1
            left.append(count_left)
 
    right = [1] 
    count_right = 1
    for i in range(len(ratings) - 2, -1, -1):
        if(ratings[i + 1] < ratings[i]):
            count_right += 1
            right.append(count_right)
        elif(ratings[i + 1] >= ratings[i]):
            count_right = 1
            right.append(count_right)
 
    right.reverse()
    sum = 0
    for i in range(len(left)):
        sum += max(left[i], right[i])
    return sum

# Better Solution Using TC - O(2N) ans SC - O(N)

def candy(ratings):
    left = [1]
    count_left = 1
    # Populating the let neighbour array   
    for i in range(1, len(ratings)):
        if(ratings[i - 1] < ratings[i]):
            count_left += 1
            left.append(count_left)
        elif(ratings[i - 1] >= ratings[i]):
            count_left = 1
            left.append(count_left)
    curr, right = 1, 1
    sum = max(1, left[-1])
    for i in range(len(ratings) - 2, -1, -1):
        if(ratings[i] > ratings[i + 1]):
            curr = right + 1
            right = curr
        else:
            curr = 1
            right = curr
        sum += max(left[i], curr)
    return sum

# Optimal Solution Using the slope 
'''
Our goal is to find the sum and not to manage the distributioni
'''
def candy(ratings):
    sum = 1
    # Starting from i = 1 as we have already taken the candy taken by the child at 0th index in consideration
    i = 1
    while(i < len(ratings)):
        # The surfae is flat
        if(ratings[i] == ratings[i - 1]):
            sum += 1
            i += 1
            continue
        # The slope increases
        # Starting with the first element as peak
        peak = 1
        while(i < len(ratings) and ratings[i] > ratings[i - 1]):
            peak += 1
            sum += peak
            i += 1
        # The slope decreases 
        down = 0
        while(i < len(ratings) and ratings[i] < ratings[i - 1]):
            down += 1
            sum += down
            i += 1
        if(down >= peak):
            sum += (down - peak + 1)
    return sum
            
            
            
            
            
        
    
            
        