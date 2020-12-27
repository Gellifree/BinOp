import random, settings, time
from main import convertToTen, convertFromTen

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
    baseCounter = 0
    for i in questions:
        numbers.append([])
    for i in range(len(numbers)):
        for j in range(exerciseCount[i]):
            if(isRegularNumber[i] == 1):
                numbers[i].append(randomValue(1)) #Átváltásnál a nehézséget 1-re állítjuk fixen, később esetleg módosítható
            elif(isRegularNumber[i] == 0):
                numbers[i].append(generateValue(exerciseBase[baseCounter], 1))
                baseCounter += 1
    print(numbers)



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
    return convertFromTen(randomValue(hardness), target, 5, False)

def draw():
    for i in range(len(questions)):
        print(str(i+1) + ") ", end="")
        print(questions[i])
        for j in range(len(numbers[i])):
            if(i < 3):
                print("   "+str(j+1)+",", numbers[i][j], "= \t? (10)")
            elif(i == 4):
                print("   "+str(j+1)+",", numbers[i][j], "= \t? (8,16)")
            else:
                print("   "+str(j+1)+",", numbers[i][j], "= \t? (" + str(exerciseHelper[j]) + ")")
        print()



#testing
def test():
    print("\nBelső feladatgenerálás\n")
    generateNumbers()
    draw()

test()
