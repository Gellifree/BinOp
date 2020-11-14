import random, settings
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
