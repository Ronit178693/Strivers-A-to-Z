# When binding characters with numbers like a=0, b=1, c=2, d=3 etc. We have to impliment it in code using ASCII values like a=97, b=98 etc. Then we can use the formular ('char' - 'a' = index in hash table) to find the corresponding value of a char in hash table.
# If there are only lowercase or only upper case letters we can take size of hash table as 26 as it reduces the space complexity

string = input("Enter the string: ")
hashtable = [0] * 256

def character_hashing(string:str, hashtable:list):
    character = input("Enter the character to find frequency: ")
    if(character not in string):
        print("Character not found in the string")
        return
    elif (len(string) == 0):
        print("Empty string")
        return
    else:
        for i in string:
            hashtable[ord(i)] += 1
    print(f"The frequency of {character} is: {hashtable[ord(character)]}")
    
character_hashing(string, hashtable)