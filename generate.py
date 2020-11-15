import random, settings, time
from main import convertToTen, convertFromTen

#Questions for the generated test
questions = [
    "Végezd el a következő átváltásokat tízes számrendszerbe: ",
    "Végezd el a következő átváltásokat tízes számrendszerből: ",
    "Végezd el az átváltást: ",
    "Végezd el az összeadást: ",
    "Végezd el a kivonást: ",
    "Végezd el a szorzást: "
]

def generateCheck():
    if(settings.GENERATE_MODE == "simple"):
        print("Generálás 'egyszerű' módra állítva.")
    elif(settings.GENERATE_MODE == "complicated"):
        print("Generálás 'bonyolult' módra állítva.")
    else:
        print("A generálás helytelen adatot tartalmaz, kérem ellenőrizze!")

def randomValue():
    if(settings.GENERATE_MODE == "simple"):
        return float(str(random.randint(0,200)) + "." + str(random.randint(0,2000)))
    elif(settings.GENERATE_MODE == "complicated"):
        return "Beállítás még nem definiált"

def generateValue(target):
    return convertFromTen(randomValue(), target, 10, False)

#testing randomnumber generator
def testGen():
    for i in range(1000000):
        print(generateValue(3), end="\r")
        time.sleep(0.1)
