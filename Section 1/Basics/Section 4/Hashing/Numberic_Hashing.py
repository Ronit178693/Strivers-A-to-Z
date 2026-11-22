size = int(input("Enter the size of the array: "))
array = [int(x) for x in input("Enter the numbers: ").split(',')]
if(len(array) != size):
    print("Invalid input")
    array = []
frequency_array = [0] * (max(array) + 1)
def find_frequency(array:list, frequency_array:list):
    num = int(input("Enter the number to find frequency: "))
    if(num not in array):
        print("Number not found in the array")
        return
    else:
        for i in range(len(array)):
            frequency_array[array[i]] += 1
    print(f"The frequency of {num} is: {frequency_array[num]}")
            
            
find_frequency(array, frequency_array)



# array = [int(x) for x in input("Enter the element: ").split(', ')]
# hash_table = [0] * (max(array) + 1)

# def find_frequency(array:list, hash_table:list):
#     for i in range(len(array)):
#         hash_table[array[i]] += 1
#     for i in array:
#         print(f'The frequency of {i} is: {hash_table[i]}')

# find_frequency(array, hash_table)
