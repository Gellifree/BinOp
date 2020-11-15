import random, settings, time
from main import convertToTen, convertFromTen

#Questions for the generated test
questions = [
    "Végezd el a következő átváltásokat tízes számrendszerből: ",
    "Végezd el a következő átváltásokat tízes számrendszerbe: ",
    "Végezd el az átváltást: ", # Bármilyen alapból bármilyen alapba - random kéne generálni ezt is
    "Végezd el az összeadást kettes számrendszerben: ",
    "Végezd el a kivonást kettes számrendszerben: ",
    "Végezd el a szorzást: "
]

numbers = []
exerciseCount = [3,3,1,2,2,2] # Hány számot kell generálni egy adott feladathoz
exerciseHardness = [1,1,2,0,0,0] # Az adott feladatok "nehézségét" állítja be, hogy ne két hatalmas számot kelljen összeszorozni, de átváltani ne 20 alattit
isRegularNumber = [1,0,0,1,1,0] # Azt állítja be, hogy tízes alapon, vagy N alapon kell-e generálni. Az 1, a tízes alapot jelöli
exerciseBase = [2,8,16,2,2,2] # Azt állítja be amennyiben nem tízes az alap, akkor mennyi

def generateNumbers():
    baseCounter = 0
    for i in questions:
        numbers.append([])
    for i in range(len(numbers)):
        for j in range(exerciseCount[i]):
            if(isRegularNumber[i] == 1):
                numbers[i].append(randomValue(exerciseHardness[i]))
            elif(isRegularNumber[i] == 0):
                numbers[i].append(generateValue(exerciseBase[baseCounter], exerciseHardness[i]))
                baseCounter += 1
    print(numbers)
    # Észrevétel potenciális hibára: Néha az egészrész üres, és a tizedespont az első karakter.


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

#testing randomnumber generator
def testGen():
    generateNumbers()

testGen()
