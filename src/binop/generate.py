import random
import time
import os

from binop import settings
from binop import converter

cnt = converter.Converter()

#Questions for the generated test
questions = [
    "Feladat (2)->(10)\n",
    "Feladat (8)->(10)\n",
    "Feladat (16)->(10)\n",
    "Feladat (10)->(n)\n",
    "Feladat (2)->(8,16)\n",
]

numbers = []
exerciseCount = [2,2,2,3,1] # Hány számot kell generálni egy adott feladathoz
isRegularNumber = [0,0,0,1,0] # Azt állítja be, hogy tízes alapon, vagy N alapon kell-e generálni. Az 1, a tízes alapot jelöli
exerciseBase = [2,2,8,8,16,16,2] # Azt állítja be amennyiben nem tízes az alap, akkor mennyi
exerciseHelper = [2,8,16]


def generateNumbers():
    numbers_ = []
    baseCounter = 0
    for i in questions:
        numbers_.append([])
    for i in range(len(numbers_)):
        for j in range(exerciseCount[i]):
            if(isRegularNumber[i] == 1):
                numbers_[i].append(randomValue(1)) #Átváltásnál a nehézséget 1-re állítjuk fixen, később esetleg módosítható
            elif(isRegularNumber[i] == 0):
                numbers_[i].append(generateValue(exerciseBase[baseCounter], 1))
                baseCounter += 1
    return numbers_



def generateCheck():
    if(settings.GENERATE_MODE == "simple"):
        print("Generálás 'egyszerű' módra állítva.")
    elif(settings.GENERATE_MODE == "complicated"):
        print("Generálás 'bonyolult' módra állítva.")
    else:
        print("A generálás beállítása helytelen adatot tartalmaz, kérem ellenőrizze!")

def randomValue(hardness):
    if(settings.GENERATE_MODE == "simple"):
        if(hardness == 0):
            return float(str(random.randint(0,20)) + "." + str(random.randint(0,100)))
        elif(hardness == 1):
            return float(str(random.randint(20,100)) + "." + str(random.randint(100,1000)))
        elif(hardness == 2):
            return float(str(random.randint(100,300)) + "." + str(random.randint(500,2000)))

    elif(settings.GENERATE_MODE == "complicated"):
        return "Beállítás még nem definiált"

def generateValue(target, hardness):
    return cnt.convertFromTen(randomValue(hardness), target, 5, False)

def drawFromArray(array):
    for i in range(len(questions)):
        print(str(i+1) + ") ", end="")
        print(questions[i])
        for j in range(len(array[i])):
            if(i < 3):
                print("   "+chr(97 + j)+",", array[i][j], "= \t? (10)")
            elif(i == 4):
                print("   "+chr(97 + j)+",", array[i][j], "= \t? (8,16)")
            else:
                print("   "+chr(97 + j)+",", array[i][j], "= \t? (" + str(exerciseHelper[j]) + ")")
        print()


def drawFromFile(file):
    exercises = []
    helper = ""
    for i in range(len(file)):
        if(file[i] == "&"):
            exercises.append(helper)
            helper = ""
        else:
            helper += file[i]
    fileNumbers = []
    for i in range(len(exercises)):
        fileNumbers.append([])

    index = 0
    for exercise in exercises:
        helper = ""
        for i in range(len(exercise)):
            if(exercise[i] == ";"):
                fileNumbers[index].append(helper)
                helper = ""
            else:
                helper += exercise[i]
        index += 1
    drawFromArray(fileNumbers)
    return fileNumbers

def testSave(array):
    file = ""
    for exercise in array:
        for number in exercise:
            file += str(number) + ";"
        file += "&"
    return file

def save(fileName):
    f = open("exercises/" + fileName + ".team3", "w")
    data = test()
    f.write(data + "\n")
    f.close()


#testing
def test():
    numbers = generateNumbers()
    file = testSave(numbers)
    return file
    #drawFromFile(file)


if(__name__ == "__main__"):
    test()
