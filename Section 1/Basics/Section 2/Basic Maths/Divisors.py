n = int(input("Enter a number: "))
for i in range(1, n+1):
    if(n%i == 0):
        print(i)
        
# TC = O(n)

#After some mathimatical observation we find out that we can find all the divisors of the number in O(sqrt(n)) time complexity. The idea is to loop from 1 to sqrt(n) and for every i, we check if it divides n or not. If it divides, then we print both i and n/i as divisors of n.

for i in range(1, int(n**0.5)+1):
    if(n%i == 0):
        print(i)
        if(i != n//i):
            print(n//i)