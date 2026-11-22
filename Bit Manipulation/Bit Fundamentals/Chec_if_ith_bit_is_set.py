# Bryte force solution 
def set_or_not(num:int, i:int):
    # Convert the number to its binary formate 
    number = []
    while(num != 1):
        remander = num % 2
        number.append(remander)
        num = num//2
  
    if(number[i] == 1):
        return True
    return False

# Optimal Solution using left shift
def set_ot_not(num, n):
    checker = 1 << n
    if((num and checker) != 0):
        return True
    return False

# Optimal solution using right shift 

def set_ot_not(num, n):
    right_shifted = num >> n
    if((right_shifted and 1) != 0):
        return True
    return False
    