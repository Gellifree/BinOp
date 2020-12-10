import main

def bitAdd(bitList):
    #Egy olyan lista összeadása, amiben "bitek" lesznek, de a carry pl. nem "kettes" alapon lesz.
    sum = numberSum(bitList)
    result = main.convertFromTen(sum,2,2,False)
    result = main.readBackwards(result)
    return result

def numberSum(list):
    sum = 0
    for item in list:
        sum += int(item)
    return sum

#Még mindig csak egész rész-re!
def binaryAdd(numberList, drawed):
    #Másolat képzése, hogy ne bántsuk a kapott listát
    copyNumberList = []
    for number in numberList:
        copyNumberList.append(number)


    binaryAddResult = "" #Ebben lesz az összeadás végső eredménye
    #Kell az eredmény hosszúsága, hogy ne legyen indexelési gond, és nullákkal ki tudjuk tölteni
    #Ahelyett hogy a leghoszabb számot néznénk, ami hibát okozna számos esetben
    #Kiszámoljuk előre az eredmény hosszát, így nem futunk később hibába

    #Konvertáljuk át Tíz-be
    numbersInTen = []
    for i in range(len(copyNumberList)):
        numbersInTen.append(main.convertToTen(copyNumberList[i], 2, False))
    #Vegyük az összeget
    sum = numberSum(numbersInTen)
    #Konvertáljuk át az összeget, majd vegyük a hosszát
    resultLen = len(main.convertFromTen(sum, 2, 0, False))
    #Megvan mekkora lesz az eredmény, mennyi nullával kell pótolni

    #Megfordítjuk a számokat, mivel "hátulról" kell számolnunk
    for i in range(len(copyNumberList)):
        copyNumberList[i] = main.readBackwards(copyNumberList[i])
    #Pótoljuk ki a számokat a megfelelő hosszig nullákkal
    for i in range(len(numberList)):
        for zero in range(resultLen - len(copyNumberList[i])):
            copyNumberList[i] += "0"

    #Hozzuk létre a carry-ért felelős listát, és töltsük fel végig nullákkal
    carry = []
    for i in range(resultLen):
        carry.append("0")

    #Képezzük az egymás "alatt" lévő bitek listáját
    for i in range(resultLen):
        bitList = []
        for j in range(len(copyNumberList)):
            bitList.append(copyNumberList[j][i])
        #Fűzzük hozzá a megfelelő helyen lévő carry "bit"-et is.
        bitList.append(carry[i])
        #Végezzük el a bitek összeadását
        bitResult = bitAdd(bitList)
        #print("Aktuális bitek:",bitList)
        #print("Bitek eredménye:",bitResult)

        #Majd hozzáfűzzük az eredményhez a leírandó számot, ami mindig a nulladik elem lesz.
        binaryAddResult += bitResult[0]
        #Ha van maradék, akkor adjuk hozzá a carry megfelelő pozíciójára (4 esetén pl eggyel arébb csúszik a szokásosnál)
        if(len(bitResult) > 1):
            for b in range(1,len(bitResult)):
                carry[i + b] = str(int(carry[i + b]) + int(bitResult[b]))
    #A carry-ben tízes számrendszerben tároljuk az eredményt, hogy ne kelljen több "mélységben" tárolni a maradékot
    #print("A végső carry:", carry)
    binaryAddResult = main.readBackwards(binaryAddResult)

    if(drawed == True):
        print(" Az összeadás eredménye: \n")
        print(" ", main.readBackwards(carry))
        for i in range(len(copyNumberList)):
            if(i == len(copyNumberList) -1):
                print("+", main.readBackwards(copyNumberList[i]))
            else:
                print(" ",main.readBackwards(copyNumberList[i]))
        for length in range(resultLen + 2):
            print("-", end="")
        print()
        print(" ", binaryAddResult, "\n")
    return binaryAddResult

# Megszámoljuk a kettespont utánni méreteket, nem feltétlenül a törtrész ugyan, ha megvan fordítva a szám!
def countFraction(number):
    index = 0
    counter = 0

    #Egyáltalán van-e benne törtrész
    if(main.checkIfFractionExist(number) == True):
        #Elmegyünk a kettedesig
        while(number[index] != "."):
            index += 1
        index += 1
        #Megszámoljuk mekkora a "maradék", ami ez esetben minden ami a törtrész
        while(index < len(number)):
            counter += 1
            index += 1
    return counter

#Az összeadadnó számokból, nézzük meg hogy mekkora a leghoszabb törtrész
def longestFraction(numberList):
    max = 0
    for number in numberList:
        index = 0
        counter = 0
        counter = countFraction(number)
        #Keresünk egy maximumot
        if(counter > max):
            max = counter
    return max

def fillWithZeroes(number, size):
    if(main.checkIfFractionExist(number) == False):
        number += "."
    for i in range(size - countFraction(number)):
        number += "0"
    return number

def searchPoint(number):
    number = main.readBackwards(number)
    result = 0
    if(main.checkIfFractionExist(number) == True):
        for point in range(len(number)):
            if(number[point] == "."):
                result = point
    return result

def binaryAddWithFraction(numberList):
    #Másolat képzése, hogy ne bántsuk a kapott listát
    copyNumberList = []
    for number in numberList:
        copyNumberList.append(number)
    #Megnézzük mekkora a legnagyobb törtrész, és kipótoljuk a többit
    size = longestFraction(copyNumberList)
    for i in range(len(copyNumberList)):
        copyNumberList[i] = fillWithZeroes(copyNumberList[i], size)
    print(copyNumberList)
    #Megkeressük hol van a kettedespontunk
    dotPlace = searchPoint(copyNumberList[0])
    print("kettedespont helye:", dotPlace)

    #Készítünk egy újabb másolatot, amiben nincs benne a kettedespont
    dotCopy = []
    for i in range(len(copyNumberList)):
        dotCopy.append("")

    for i in range(len(copyNumberList)):
        for j in range(len(copyNumberList[i])):
            if(copyNumberList[i][j] != "."):
                dotCopy[i] += copyNumberList[i][j]
    print(dotCopy)
    #Végezzük el az összeadást mint ha ezek rendes 'egész' számok lennének
    #Itt lesz valami gubanc, hiszen az összeadás módszere miatt, sokkal "nagyobb" számokat néz,
    #és lehet ebből adódik egy feleslegesen nagy kipótlás nullákkal.
    #Mivel módosítani kell pár dolgon, ezért inkább legyen egy pici redundancia, amit esetleg később feloldunk
    addition = binaryAdd(dotCopy, True)
    print(addition)
    result = ""
    for i in range(len(addition)):
        if(i != len(addition) - dotPlace):
            result += addition[i]
        else:
            result += "." + addition[i]
    print(result)
    return result

#fractionTest = ["111.1", "11.1"]
#print("A legnagyobb fraction:",longestFraction(fractionTest))
#print("\n")
#binaryAddWithFraction(fractionTest)

numbers = ["111", "11"]

test = binaryAdd(numbers, True)

print("Az összeadás eredménye:", test, "azaz", main.convertToTen(test, 2, False))
