num = int(input("Enter the number: "))

def fibunacci(num:int):
    if(num<=1):
        return num
    else:
        return fibunacci(num-1) + fibunacci(num-2)
    
print(fibunacci(num))