n = int(input("Enter a number: "))
count = 0
for i in range(1, n+1):
    if(n%i == 0):
        count += 1
if(count == 2):
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")
    
# We can find all the divisors of a number even if we loop till sqrt(n)

count = 0
for i in range(1,int(n**0.5)+1):
    if(n%i == 0):
        count += 1 
        if(i != n//i):
            count += 1
if(count == 2):
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")