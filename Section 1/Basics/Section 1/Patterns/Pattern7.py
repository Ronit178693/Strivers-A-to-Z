'''
The order for spaces and stars is as follows:

[4, 1, 4]
[3, 3, 3,]
[2, 5, 2]
[1, 7, 1]
[0, 9, 0]

[n-i-1, 2i+1, n-i-1]

'''


for i in range(5):
    # n-i-1 for the widespaces
    for j in range(5-i-1):
            print(" ", end = "")
    # 2i+1 for the stars 
    for j in range(2*i+1):
        print("*", end = "")
    for j in range(5-i-1):
            print(" ", end = "")
    print("\n")