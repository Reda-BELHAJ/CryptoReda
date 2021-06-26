LIMITS_Upp = (65, 90)
LIMITS_Dwn = (97, 122)

def lenList(inputStr):
    return [i for i in range(len(inputStr))]

def getNumbers(inputStr):
    numbers   = [int(char) for char in inputStr if char.isdigit()]

    numbers += lenList(inputStr)

    return numbers

def transformnumbers(inputStr, function):
    res_str = ""
    numbers = function(inputStr)

    for num in numbers:
        res_str += chr(num + LIMITS_Dwn[0])
        
    return res_str

def hasNumbers(inputStr):
    return any(char.isdigit() for char in inputStr)

def getEO(inputStr):
    return inputStr[::2], inputStr[1::2]

def transformIn(inputStr, keyStr):
    input    =  inputStr[::-1]
    input   += keyStr
    hash_str = getEO(input)[0] + getEO(input)[1]

    return hash_str

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


input = "JHEae1a5ALBdRdd4fdbebecaf"
key = "1dad54"
key2 = "dsa"

decrypt(input, key)