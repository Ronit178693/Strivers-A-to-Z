# Setting the ith bit means toggling it to 1 

# Using the left shift operator
def set_to_1(num, i):
    checker = 1 << i
    num = num or checker
    