import math

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def getNumbers(inputString):
    return [char for char in inputString if char.isdigit()]

def encrypt(input: str, key: str):
    hash_str = ""
    input    =  input[::-1]
    
    if hasNumbers(key):
        numbers   = getNumbers(key)
    else:
        pass

    return hash_str

def decrypt(input: str, key: str):
    pass


input = "Test"
key = "1dad5"

# print(encrypt(input, key))