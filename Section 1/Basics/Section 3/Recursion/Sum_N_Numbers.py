N = int(input("Enter a number: "))

def Sum(N:int, sum:int = 0):
    if(N<=0):
        return sum
    else:
        sum = sum + N
        return Sum(N-1, sum)
       
print(Sum(N))

# Soultion to the problem wihtout using an extra variable sum

def Sum(N:int):
    if(N<=0):
        return 0
    return N + Sum(N-1)
print(Sum(N))
    