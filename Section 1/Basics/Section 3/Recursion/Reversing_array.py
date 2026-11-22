Numbers = [int(x) for x in input().split(',')]

# Using 2 pointer approache
def reverse(Numbers:list, i:int = 0, j:int = len(Numbers)-1):
    if(i>=j):
        return Numbers
    else:
        Numbers[i], Numbers[j] = Numbers[j], Numbers[i]
        return reverse(Numbers, i+1, j-1)
print(reverse(Numbers))

# Reversing an array using only 1 pointer 
# Replacing i th element with n-i-1 th element 

def Reverse(Numbers:list, i:int = 0):
    if(i>= len(Numbers)//2):
        return Numbers
    else:
        Numbers[i], Numbers[len(Numbers)-i-1] = Numbers[len(Numbers)-i-1], Numbers[i]
        return Reverse(Numbers, i+1)
print(Reverse(Numbers))