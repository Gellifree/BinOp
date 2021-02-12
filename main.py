#!/usr/bin/python3.8

#importing needed resources
import os, generate, solver, menu
from sys import platform
import settings as st

md = menu.MenuDrawer()

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
    if(drawed == False):
        i = 0
        while (i < len(number)):
            result += (base**(-(i+1))) * safetyConvert(number[i])
            i += 1
        return result
    else:
        print("  Törtrész számítása\n")
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


def convertingNumbers():
    miniMenu = ["Átváltás tízes számrendszerből","Átváltás tízes számrendszerbe"]
    miniexec = [fromTen, toTen]
    answer = md.draw(miniMenu)
    print(" >>", miniMenu[int(answer)], "<< ")
    miniexec[answer]()

def fromTen():
    print("  Add meg a számot, amit át szeretnél váltani!")
    number = input("  >> ")
    print("  Add meg a célszámrendszer alapját, amibe átszeretnéd váltani! [2-16]")
    #We could give the user a menu maybe
    target = int(input("  >> "))
    precision = 0
    if(checkIfFractionExist(number) == True):
        print("  Add meg a tizedes érték kiszámításának pontosságát!")
        precision = int(input("  >> "))
        number = float(number)
    else:
        number = int(number)
    print("  Látni akarod a számítás részleteit? [Y/n]")
    drawed = input("  >> ")
    if(drawed == "y" or drawed == "" or drawed == "Y"):
        drawed = True
    else:
        drawed = False


    print("\n  Az átváltás eredménye: ", convertFromTen(number, target, precision, drawed))

def toTen():
    print("  Add meg a számot, amit átszeretnél váltani tízes alapúvá!")
    number = input("  >> ")
    print("  Add meg hogy ez a szám milyen számrendszerben értelmezett! [2-16]")
    #We could give the user a menu maybe?
    target = int(input("  >> "))
    print("  Látni akarod a számítás részleteit? [Y/n]")
    drawed = input("  >> ")
    if(drawed == "y" or drawed == "" or drawed == "Y"):
        drawed = True
    else:
        drawed = False
    print(" Az átváltás eredénye: ", convertToTen(number, target, drawed))

def exercises():
    miniMenu = ["Feladatsor generálása", "Feladatsorok megtekintése"]
    miniexec = [genExcercise, lookExcercise]

    answer = md.draw(miniMenu)
    print(" >>",miniMenu[answer], "<<")
    miniexec[answer]()

def genExcercise():
    fileName = input("   >> Milyen néven kívánja elmenteni a feladatsort?: ")
    generate.save(fileName)
    print("   >> Fájl elmentve! <<")

def lookExcercise():
    paths = []
    fileNames = []

    result = []

    with os.scandir("exercises") as it:
        for entry in it:
            if entry.name.endswith(".team3") and entry.is_file():
                paths.append(entry.path)
                fileNames.append(entry.name)
    if(len(paths) == 0):
        print("    >> Nincsenek lementett feladatsorok! Kérem generáljon feladatsorokat! <<")
    else:
        print("   >> Melyik lementett feladatsort szeretné megtekinteni?\n")
        answer = md.draw(fileNames)

        f = open(paths[answer], "r")
        data = f.read()
        f.close()
        print("   >> A kiválasztott feladatsor <<\n")
        result = generate.drawFromFile(data)
    print("  Látni akarod a feladatsor megoldását? [Y/n]")
    solution = input("  >> ")
    if(solution == "y" or solution == "" or solution == "Y"):
        solver.solveExercises(result)


def complementer():
    print(" Komplementerképzésért felelős menüpont")


def binaryAnd():
    print("  Bináris ÉS műveletért felelős menüpont")

def binaryOr():
    print("  Bináris VAGY műveletért felelős menüpont")

def ipCheck():
    print("  Két IP cím ellenőrzése")

def binaryOperations():
    binaryMenu = ["Bináris ÉS", "Bináris VAGY", "IP ellenőrzés"]
    functionMenu = [binaryAnd, binaryOr, ipCheck]

    answer = drawMenu(binaryMenu)
    functionMenu[int(answer)]()


def huffman():
    print(" Huffman kódolási eljárás későbbi menüpontja")

def settings():
    print("  Beállítások\n")
    print(" >> Képernyő tisztítás módja <<")
    print("    [X] (N)ecessery\t[-] (A)lways")

    print()

    print(" >> Rész számítások megjelenítése <<")
    print("    [X] A(s)k\t\t[-] A(l)ways\t[-] N(e)ver")

def help():
    print(" Későbbi segítségeket, és információkat tartalmazó menüpont")

def main():
    mainMenu = ["Átváltás", "Feladatsorok", "Komplementerképzés", "Bináris műveletek","Huffman" ,"Beállítások", "Segítség", "Kilépés"]
    functionMenu = [convertingNumbers, exercises, complementer, binaryOperations, huffman, settings, help]

    answer = 0
    while(answer != -1):
        os.system("clear")

        if(platform == "linux" or platform == "linux2"):
            width = os.get_terminal_size().columns
            middleText = "BinOp\n"
            os.system("setterm -foreground blue")
            print("Python 3.6.9", end="")
            print(middleText.center(width-len(middleText)))
            os.system("setterm -foreground white")
        elif(platform == "win32"):
            print("BinOp - Bináris Operációk\n")

        answer = md.draw(mainMenu)

        if(answer == -2 or answer == -3):
            input("  >> Nyomj entert a visszatéréshez! <<")
        elif(answer != -1):
            print(" >>" + mainMenu[answer] + " <<\n")
            functionMenu[answer]()
            input(" >> Kész <<")
        else:
            input(" >> A program most kilép <<")
            os.system("clear")

if(__name__ == "__main__"):
    main()
