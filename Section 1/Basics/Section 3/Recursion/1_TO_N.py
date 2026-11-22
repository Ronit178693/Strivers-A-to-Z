n = int(input("Enter a number: "))
def Linearly(n:int, i:int = 1):
    if(i>n):
        return
    else:
        print(i)
        Linearly(n, i+1)
Linearly(n)
    
    
# Using Backtracking
