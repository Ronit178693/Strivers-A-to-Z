'''
The order for spaces and stars is as follows:

[3, 1, 3]
[2, 3, 2]
[1, 5, 1]
[0, 7, 0]

[n-i, 2*(i)+1, n-i]

'''
char = 'A'

for i in range(4):
    for j in range(4-i):
        print(" ", end = "")
    for j in range(2*i+1):
        print(chr(65+j), end = "")
    for j in range(4-i):
        print(" ", end = "")
    print("\n")