LIMITS_Upp = (65, 90)
LIMITS_Dwn = (97, 122)

def hasNumbers(inputStr):
    return any(char.isdigit() for char in inputStr)

def getEO(inputStr):
    return inputStr[::2], inputStr[1::2]

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


def transformIn(inputStr, keyStr):
    input    =  inputStr[::-1]
    input   += keyStr
    hash_str = getEO(input)[0] + getEO(input)[1]

    return hash_str


def encrypt(input: str, key: str):
    hash_str = transformIn(input, key)
    
    if hasNumbers(key):
        res_str   = transformnumbers(key, getNumbers)
        hash_str += transformIn(res_str, "")
    else:
        res_str  = transformnumbers(key, lenList)
        hash_str += transformIn(res_str, "")

    return hash_str