import main

def bitAdd(bitList):
    sum = 0
    for i in range(len(bitList)):
        sum += int(bitList[i])
    result = main.convertFromTen(sum,2,2,False)
    result = main.readBackwards(result)
    return result

def maxLenSearch(list):
    result = ""
    for i in range(len(list)):
        if(len(list[i]) > len(result)):
            result = list[i]
    return result

#Csak egész számokra
def binaryAdd(numberList):
    for i in range(len(numberList)):
        numberList[i] = main.readBackwards(numberList[i])
    maxLen = len(maxLenSearch(numberList)) + 1 #Csak addig működik az összeadás, amíg az összegek nem lépik át két bitnyivel a leghoszabb számot!
    for i in range(len(numberList)):
        for zero in range(0, maxLen - len(numberList[i])):
            numberList[i] += "0"
    print(numberList)
    carry = []
    for i in range(maxLen + 1):
        carry.append("0")
    print("carry:",carry)

    result = ""
    for i in range(maxLen):
        bitList = []
        for j in range(len(numberList)):
            bitList.append(numberList[j][i])
        bitList.append(carry[i])
        print(bitList)
        bitresult = bitAdd(bitList)
        print(bitresult,"\n")
        result += bitresult[0]
        if(len(bitresult) > 1):
            for b in range(len(bitresult)):
                carry[i + b] = bitresult[b]
    return main.readBackwards(result)


bits = ["1","1","1","1","1","1"]
print(bitAdd(bits))

numbers = ["111100", "0", "0","1"]
result = binaryAdd(numbers)
print(result)
print("Visszaváltva: ", main.convertToTen(result, 2, False))
