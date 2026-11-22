# Brute Force
def missing(arr:list = [1, 2, 4, 3], n:int = 5):
    
    for i in range(1, n+1):
        flagged = 0 # Storing the number of occurence
        for j in range(len(arr)):
            if(arr[j] == i):
                flagged += 1
                break
        if(flagged == 0):
            return i
        
print(missing())

'''
TC - O(N^2)
SC - O(1)
'''

# Better Solution

def missing(arr:list = [1, 2, 4, 3], n:int = 5):
    frequency = [0] * n+1
    for i in range(len(arr)):
        frequency[arr[i]] = 1
    for i in range(1, len(frequency)):
        if(frequency[i] == 0):
            return i
    
print(missing())


'''
TC = O(2N)
SC = O(N)
'''
           
           
# Optimal Solution 

def missing(arr:list = [1, 2, 4, 3], n:int = 5):
    sum1 = len(n)*((len(n)+1)/2)
    sum2 = 0
    
    for j in arr:
        sum2 += j
    return sum1 - sum2
print(missing())

'''
TC = O(N)
SC = O(1)
'''
