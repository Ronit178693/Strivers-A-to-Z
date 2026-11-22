'''
The order for spaces and stars is as follows:

[0, 9, 0]
[1, 7, 1]
[2, 5, 2]
[3, 3, 3]
[4, 1, 4]

[i, 2n-2i-1, i]

'''



for i in range(5):
    for j in range(i):
        print(" ", end = "")
    for j in range(2*5-2*i-1):
        print("*", end = "")
    for j in range(i):
        print(" ", end = "")
    print("\n")