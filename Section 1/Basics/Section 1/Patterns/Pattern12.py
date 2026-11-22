'''
The order for spaces and stars is as follows:

[1, 6, 1]
[2, 4, 2]
[3, 2, 3]
[4, 0, 4]

[i, 2(n-i-1), i]

'''
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end = "")
    for j in range(2*(4-i)):
        print(" ", end = "")
    for j in range(i, 0, -1):
        print(j, end = "")
    print("\n")