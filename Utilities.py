import math
import random

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def getEO(inputString):
    return inputString[::2], inputString[1::2]

def getNumbers(inputString):
    numbers   = [char for char in inputString if char.isdigit()]
    nums      = []

    for i in range(len(inputString)):
        nums.append(i)

    numbers += nums

    return numbers

def encrypt(input: str, key: str):
    hash_str = ""
    input    =  input[::-1]
    input   += key
    even_str, odd_str  = getEO(input)
    hash_str = even_str + odd_str
    
    if hasNumbers(key):
        numbers = getNumbers(key)
        print(numbers)
    else:
        pass
    return hash_str

def decrypt(input: str, key: str):
    pass


input = "Test"
key = "1dad54"

print(encrypt(input, key))