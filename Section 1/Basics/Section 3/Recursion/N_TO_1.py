n = int(input("Enter the number: "))
def Linear(n:int):
    if(n<=0):
        return
    print(n)
    Linear(n-1)

Linear(n)