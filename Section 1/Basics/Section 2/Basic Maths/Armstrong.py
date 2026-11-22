n = int(input("Enter a number: "))

original = n
sum = 0
while(n != 0):
    digit = n%10
    n //= 10
    sum = sum + (digit**3)

if(original == sum):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")