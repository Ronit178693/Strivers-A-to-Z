N = int(input("Enter the number: "))

def Factorial(N:int):
    if(N == 1 or N == 0):
        return 1
    return N*Factorial(N-1)
print(Factorial(N))