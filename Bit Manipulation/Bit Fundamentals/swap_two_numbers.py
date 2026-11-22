# Swapping 2 numbers without using a third variable 
def swap_numbers(a:int, b:int):
    a = a ^ b
    b = a ^ b
    a = a ^ b
'''
a = a^b
b = a^b = a^b^b = a
a = a^b = a^b^a = b
which reversed both a and b
'''


    