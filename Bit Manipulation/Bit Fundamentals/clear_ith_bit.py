# Clearing the bit means changing it to 0
def clear(num, i):
    checker = not(1 << i)
    num and checker
    
    