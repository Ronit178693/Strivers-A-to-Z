n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
gcd = 1 # When checking for HCF both the numbers wil lhave 1 as a common factor atleast

for i in range(1, min(n1, n2)+1): # Using min(n1, n2) because its if a number is a factor of both n1 and n2 then it will be less than or equal to the minimum of the two numbers
    if(n1%i == 0 and n2%i == 0):
        gcd = i
print("The GCD of", n1, "and", n2, "is", gcd)

for i in range(min(n1, n2), 0, -1): # Using min(n1, n2) because its if a number is a factor of both n1 and n2 then it will be less than or equal to the minimum of the two numbers
    if(n1%i == 0 and n2%i == 0):
        gcd = i
        break # We can break here because we are starting from the maximum number and going downwards so the first number we find will be the GCD
    
print("The GCD of", n1, "and", n2, "is", gcd)