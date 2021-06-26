from encryption import *

def getED(inputStr):
    return inputStr[:int(len(inputStr)/2)], inputStr[int(len(inputStr)/2):]

def transformOut(inputStr):
    str1, str2 = getED(inputStr)
    result = ""
    i = 0

    while (i < len(str1)) or (i < len(str2)):
        if (i < len(str1)):
            result += str1[i]

        if (i < len(str2)):
            result += str2[i]
             
        i += 1
    
    return result

def decrypt(input: str, key: str):
    hash_str = ""

    if hasNumbers(key):
        res_str   = transformnumbers(key, getNumbers)
        hash_str += transformIn(res_str, "")
    else:
        res_str  = transformnumbers(key, lenList)
        hash_str += transformIn(res_str, "")
    
    input = input.replace(hash_str, '')
    result = transformOut(input).replace(key, '')[::-1]

    return result