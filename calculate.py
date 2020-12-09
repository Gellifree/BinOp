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

def numberSum(list):
    sum = 0
    for item in list:
        sum += item
    return sum

def binaryAdd(numberList):
    binaryAddResult = ""
    #Kell az eredmény hosszúsága, hogy ne legyen indexelési gond, és nullákkal ki tudjuk tölteni
    #Ahelyett hogy a leghoszabb számot néznénk, ami hibát okozna számos esetben
    #Kiszámoljuk előre az eredmény hosszát, így nem futunk később hibába

    #Konvertáljuk át Tíz-be
    numbersInTen = []
    for i in range(len(numberList)):
        numbersInTen.append(main.convertToTen(numberList[i], 2, False))
    #Vegyük az összeget
    sum = numberSum(numbersInTen)
    #Konvertáljuk át az összeget, majd vegyük a hosszát
    resultLen = len(main.convertFromTen(sum, 2, 0, False))
    #Megvan mekkora lesz az eredmény, mennyi nullával kell pótolni

    #Megfordítjuk a számokat, mivel "hátulról" kell számolnunk
    for i in range(len(numberList)):
        numberList[i] = main.readBackwards(numberList[i])
    #Pótoljuk ki a számokat a megfelelő hosszig nullákkal
    for i in range(len(numberList)):
        for zero in range(resultLen - len(numberList[i])):
            numberList[i] += "0"

    #Hozzuk létre a carry-ért felelős listát, és töltsük fel végig nullákkal
    carry = []
    for i in range(resultLen):
        carry.append("0")

    #Képezzük az egymás "alatt" lévő bitek listáját
    for i in range(resultLen):
        bitList = []
        for j in range(len(numberList)):
            bitList.append(numberList[j][i])
            #Fűzzük hozzá a megfelelő helyen lévő carry "bit"-et is.
        bitList.append(carry[i])
        #Végezzük el a bitek összeadását
        bitResult = bitAdd(bitList)
        #print("Aktuális bitek:",bitList)
        #print("Bitek eredménye:",bitResult)
        binaryAddResult += bitResult[0]
        #Ha van maradék, akkor adjuk hozzá a carry megfelelő pozíciójára (4 esetén pl eggyel arébb csúszik a szokásosnál)
        if(len(bitResult) > 1):
            for b in range(len(bitResult)):
                carry[i + b] = str(int(carry[i + b]) + int(bitResult[b]))
    #A carry-ben tízes számrendszerben tároljuk az eredményt, hogy ne kelljen több "mélységben" tárolni a maradékot
    print("A végső carry:", carry)
    binaryAddResult = main.readBackwards(binaryAddResult)
    print("Az összeadás eredménye:", binaryAddResult, "azaz", main.convertToTen(binaryAddResult, 2, False))

numbers = ["111", "111", "111","111","111","111","1"]
binaryAdd(numbers)
