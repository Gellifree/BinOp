#importing needed resources
import os, settings, main
from sys import platform



def flip(jegy):
    if jegy == "1" :
        return "0"
    else :
        return "1"


def oneComplementer(number):


    egyeskomplementer = main.convertFromTen(number, 2, 3, False)
    print(egyeskomplementer)
    i = 0
    result = ""

    while i < len(egyeskomplementer):
        result += flip(egyeskomplementer[i])
        i += 1

    print("az eredmeny:", result)

    return result

# vigyazat! csak binárisan értelmezhető számokat kaphat
def additionBinary(x, y):
    x = str(x)
    y = str(y)
    max_len = max(len(x), len(y))

    x = x.zfill(max_len)
    fractionPosition = -1
    if main.checkIfFractionExist(x) == True:
        fractionPosition = searchFraction(x)
    y = y.zfill(max_len)

    print("az x:", x, "Az y: ", y)

    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        c = carry
        c += 1 if x[i] == '1' else 0
        c += 1 if y[i] == '1' else 0
        result = ('1' if c % 2 == 1 else '0') + result
        carry = 0 if c < 2 else 1

    if carry != 0: result = '1' + result

    finalResult = ""
    for i in range(len(result)):
        if i == fractionPosition:
            finalResult += "."
        else:
            finalResult += result[i]
    return finalResult

def searchFraction(number):
    for i in range(len(number)):
        if number[i]==".":
            return i


def twoComplemeter():
    number = 8

    result = additionBinary(oneComplementer(number), "1")
    print("a szám kettes komplementere: ", result)
    return result



def mainn():
    print(additionBinary("11.10", "1000.01"))






if(__name__ == "__main__"):
    mainn()
