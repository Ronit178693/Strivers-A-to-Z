array = [int(x) for x in input("Enter the element: ").split(',')]
hash_table = [0] * (max(array) + 1)

def find_frequency(array:list, hash_table:list):
    for i in range(len(array)):
        hash_table[array[i]] += 1
    for i in array:
        print(f'The frequency of {i} is: {hash_table[i]}')
    print("The highest occuring element is: ", hash_table.index(max(hash_table)))


find_frequency(array, hash_table)
