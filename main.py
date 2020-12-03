#importing needed resources
import os, settings
from sys import platform

# Functions for drawing the menues:
def drawMenu(elements):
    index = 0
    for element in elements:
        if(element == "Kilépés"):
            print("     [Q] {}".format(element))
        else:
            print("     [{}] {}".format(index, element))
        index += 1
    print()
    answer = input(" >> ")
    if(answer == "Q" or answer == "q"):
        return answer
    elif(int(answer) < len(elements)):
        return answer
    else:
        print("  >> Nem adhatsz meg ilyen opciót! <<")
        return "error"

#Funkcions for helping calculations
def readBackwards(data):
    result = ""
    i = len(data)-1
    while(i >= 0):
        result += data[i]
        i -= 1
    return result

# data separate:
def separate(data):
    if(type(data) == str):
        result = []
        partOne = ""
        partTwo = ""
        i = 0
        while(data[i] != "."):
            partOne += data[i]
            i += 1
        i += 1
        while(i < len(data)):
            partTwo += data[i]
            i += 1
        result.append(partOne)
        result.append(partTwo)
        return result
    elif(type(data) == float):
        result = []
        partOne = 0
        partTwo = 0
        partOne = int(data)
        partTwo = data - partOne
        result.append(partOne)
        result.append(partTwo)
        return result

def checkIfFractionExist(number):
    number = str(number)
    for i in range(len(number)):
        if(number[i] == "."):
            return True
    return False

def safetyConvert(data):
    if(type(data) == str):
        result = {
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "A" : 10,
            "a" : 10,
            "B" : 11,
            "b" : 11,
            "C" : 12,
            "c" : 12,
            "D" : 13,
            "d" : 13,
            "E" : 14,
            "e" : 14,
            "F" : 15,
            "f" : 15
        }
        return result.get(data, "rorrE")
    elif(type(data) == int):
        result = {
            0 : "0",
            1 : "1",
            2 : "2",
            3 : "3",
            4 : "4",
            5 : "5",
            6 : "6",
            7 : "7",
            8 : "8",
            9 : "9",
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
        }
        return result.get(data, "rorrE")

#Calculations
def integerCalculation(number, target, drawed):
    result = ""
    if(drawed == False):
        while(number >= 1):
            result += safetyConvert(int(number % target))
            number /= target
        return readBackwards(result)
    else:
        print("\n  Egészrész kiszámolása\n")
        print("  {} % {}".format(number, target))
        print("  =====")
        while(number >= 1):
            result += safetyConvert(int(number % target))
            print("  {} | {}".format(int(number/target), int(number % target)))
            number /= target
        print("  Egészrész: ", readBackwards(result),"\n")
        return readBackwards(result)

def fractionCalculation(number, target, precision, drawed):
    result = ""
    if(drawed == False):
        i = 0
        while(i < precision):
            result += safetyConvert(separate(number*target)[0])
            number = separate(number * target)[1]
            i += 1
        return result
    else:
        i = 0
        print("\n  Törtrész kiszámolása\n")
        print("  {} * {}".format(number, target))
        print("  =======")
        while(i < precision):
            print("  {} * {} =>".format(number * target, target))
            result += safetyConvert(separate(number*target)[0])
            number = separate(number * target)[1]
            i += 1
        print("  Törtrész: ", result,"\n")
        return result

def convertFromTen(number, target, precision, drawed):
    if(checkIfFractionExist(number) == True):
        result = ""
        result += integerCalculation(separate(number)[0], target, drawed)
        if(result == ""):
            result = "0"
        result += "."
        result += fractionCalculation(separate(number)[1], target, precision, drawed)
        return result
    else:
        result = ""
        result += integerCalculation(number, target, drawed)
        if(result == ""):
            result = "0"
        return result

def integerCalculation_N(number, base, drawed):
    result = 0
    if(drawed == False):
        numberBack = readBackwards(number)
        i = 0
        while(i < len(numberBack)):
            result += (base**i) * safetyConvert(numberBack[i])
            i += 1
        return result
    else:
        numberBack = readBackwards(number)
        i = 0
        print("\n  Számítások elvégzése\n")
        while(i < len(numberBack)):
            print("  ({0}^{1}) * {2} = {3}".format(base,i,safetyConvert(numberBack[i]), (base**i)*safetyConvert(numberBack[i])))
            result += (base**i) * safetyConvert(numberBack[i])
            i += 1
        print("  Az egészrész: ", result,"\n")
        return result


def fractionCalculation_N(number, base, drawed):
    result = 0
    print("  Törtrész számítása\n")
    if(drawed == False):
        i = 0
        while (i < len(number)):
            result += (base**(-(i+1))) * safetyConvert(number[i])
            i += 1
        return result
    else:
        i = 0
        while (i < len(number)):
            print("  ({0}^({1})) * {2} = {3}".format(base, -(i+1), safetyConvert(number[i]), (base**(-(i+1)))*safetyConvert(number[i])))
            result += (base**(-(i+1)))*safetyConvert(number[i])
            i += 1
        print("  A törtrész: ", result,"\n")
        return result

def convertToTen(number, base, drawed):
    result = 0
    if(checkIfFractionExist(number) == True):
        partOne = separate(number)[0]
        partTwo = separate(number)[1]

        result = integerCalculation_N(partOne, base, drawed)
        result += fractionCalculation_N(partTwo, base, drawed)
        return result
    else:
        result = integerCalculation_N(number, base, drawed)
        return result


#Use these to check if the functions works
def fromTen():
    print("  Add meg a számot, amit át szeretnél váltani!")
    number = input("  >> ")
    print("  Add meg a célszámrendszer alapját, amibe átszeretnéd váltani! [2-16]")
    #We could give the user a menu maybe
    target = int(input("  >> "))
    print("  Látni akarod a számítás részleteit? [Y/n]")
    drawed = input("  >> ")
    if(drawed == "y" or drawed == "" or drawed == "Y"):
        drawed = True
    else:
        drawed = False
    precision = 0
    if(checkIfFractionExist(number) == True):
        print("  Add meg a tizedes érték kiszámításának pontosságát!")
        precision = int(input("  >> "))
        number = float(number)
    else:
        number = int(number)

    print("\n  Az átváltás eredménye: ", convertFromTen(number, target, precision, drawed))


def toTen():
    print("  Add meg a számot, amit átszeretnél váltani tízes alapúvá!")
    number = input("  >> ")
    print("  Add meg hogy ez a szám milyen számrendszerben értelmezett! [2-16]")
    #We could give the user a menu maybe?
    target = int(input("  >> "))
    print(" Az átváltás eredénye: ", convertToTen(number, target, True))

def genExcercise():
    print(" Későbbi feladatgenerálási menüpont.")

def lookExcercise():
    print(" Későbbi feladat megtekintő menüpont.")

def settings():
    print(" Későbbi beállítások menüpont")

def help():
    print(" Későbbi segítségeket, és információkat tartalmazó menüpont")

def main():
    mainMenu = ["Átváltás tízes számrendszerből", "Átváltás tízes számrendszerbe", "Feladatsor generálása","Feladatsorok megtekintése","Beállítások","Segítség", "Kilépés"]
    executableMenu = ["fromTen()", "toTen", "genExcercise()","lookExcercise()","settings()", "help()"]

    menuState = 0
    answer = 0
    while(answer != "q" and answer != "Q"):
        os.system("clear")

        if(platform == "linux" or platform == "linux2"):
            width = os.get_terminal_size().columns
            middleText = "Számrendszer átváltó\n"
            os.system("setterm -foreground blue")
            print("Hármas csapat", end="")
            print(middleText.center(width-len(middleText)))
            os.system("setterm -foreground white")
        elif(platform == "win32"):
            print("Számrendszer átváltó és feladatgeneráló\n")

        answer = drawMenu(mainMenu)
        if(answer == "error"):
            input("  >> Kész <<")
        elif(answer != "Q" and answer != "q"):
            menuState = int(answer)
            print(" >> " + mainMenu[menuState] + " <<\n")
            exec(executableMenu[menuState])
            input(" >> Kész <<")
        else:
            quit = input("  >> Biztos vagy benne, hogy ki szeretnél lépni? [Y/n]: ")
            if(quit == "N" or quit == "n"):
                answer = 0
            elif(quit == "" or quit == "Y" or quit == "y"):
                answer = "q"
                os.system("clear")

if(__name__ == "__main__"):
    main()
