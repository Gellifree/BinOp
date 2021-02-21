#!/usr/bin/python3.8

#importing needed resources
import os, generate, solver, menu, converter
import normalizer, operations, errorhandler
from sys import platform
import settings as st

md = menu.MenuDrawer()
cnt = converter.Converter()
nm = normalizer.Normalizer()
op = operations.Operator()
err = errorhandler.ErrorHandler()



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
    if(cnt.checkIfFractionExist(number) == True):
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


    print("\n  Az átváltás eredménye: ", cnt.convertFromTen(number, target, precision, drawed))

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
    print(" Az átváltás eredénye: ", cnt.convertToTen(number, target, drawed))

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

    print("  Kérem adja meg az első számot: ")
    number1 = input("  >> ")
    if(err.isItBinary(number1) == -1):
        print("  >> A bináris És műveletnek, csak bináris értékre van értelme! <<")
        #Később ciklusba szervezni
        return
    print("  Kérem adja meg a második számot: ")
    number2 = input("  >> ")
    if(err.isItBinary(number2) == -1):
        print("  >> A bináris És műveletnek, csak bináris értékre van értelme! <<")
        return
    result = op.binaryAnd(number1, number2)
    print("\n  >> A logikai És eredménye: ", result)

def binaryOr():
    print("  Bináris VAGY műveletért felelős menüpont")

def ipCheck():
    print("  Két IP cím ellenőrzése")

def binaryOperations():
    binaryMenu = ["Bináris ÉS", "Bináris VAGY", "IP ellenőrzés"]
    functionMenu = [binaryAnd, binaryOr, ipCheck]

    answer = md.draw(binaryMenu)
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
