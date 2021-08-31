#!/usr/bin/python3.8

#importing needed resources
#import os, generate, solver, menu, converter
#import normalizer, operations, errorhandler
from sys import platform
#import settings as st


from binop import generate
from binop import solver
from binop import menu
from binop import converter
from binop import normalizer
from binop import operations
from binop import errorhandler
from binop import settings as st
import os

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
    print("  Két IP cím ellenőrzése:")
    print("\n  >> Add meg az Alhálózati maszkot: ")
    mask = input("  >> ")
    if(err.isItValidIP(mask) < 0):
        print("  >> A megadott alhálózati maszk helytelen! <<")
        return
    print("\n  >> Add meg az feladó IP címét: ")
    ip1 = input("  >> ")
    if(err.isItValidIP(ip1) < 0):
        print("  >> A megadott Ip helytelen! <<")
        return
    print("\n  >> Add meg a címzett IP címét: ")
    ip2 = input("  >> ")
    if(err.isItValidIP(ip2) < 0):
        print("  >> A megadott Ip helytelen! <<")
        return

    print("  A két IP cím hálózata: \n")

    print("  >> Feladó:", op.ipNetwork(mask, ip1))

    print("\n  >> Címzett:", op.ipNetwork(mask, ip2))
    if(op.ipNetwork(mask, ip1) == op.ipNetwork(mask, ip2)):
        print("  >>> A hálózat megeggyezik <<<")


def binaryOperations():
    binaryMenu = ["Bináris ÉS", "Bináris VAGY", "IP ellenőrzés"]
    functionMenu = [binaryAnd, binaryOr, ipCheck]

    answer = md.draw(binaryMenu)
    functionMenu[int(answer)]()

def networkCheck():
    print("  Add meg a hálózat Ip-jét: ")
    network = input("  >> ")
    if(err.isItValidIP(network) < 0):
        print("  >>> A hálózati címben elírás történt! <<<")
    else:
        print("\n  Milyen címosztályban értelmezett? (A,B,C): ")
        class_asnwer = input("  >> ")
        if(err.isItValidClass(class_asnwer) == -1):
            print("  >>> A megadott osztály nem helytálló ebben a kontextusban! <<<")
        else:
            networkMask = ""
            if(class_asnwer == "A" or class_asnwer == "a"):
                networkMask = "255.0.0.0"
            elif(class_asnwer == "B" or class_asnwer == "b"):
                networkMask = "255.255.0.0"
            elif(class_asnwer == "C" or class_asnwer == "c"):
                networkMask = "255.255.255.0"
            else:
                networkMask = "Error"

            result = op.ipDatas(network)

            print("\n  >> A megadott IP:\t", result["ip"])
            print("  >> Binárisban: \t", op.ipInBinary(result["ip"]))
            print("\n  >> A Sub. Mask:\t", networkMask)
            print("  >> A Gateway:   \t", result["gateway"])
            print("  >> A Broadcast: \t", result["broadcast"])
            print("  >> Devices:     \t", result["devices"], "\n")


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
    mainMenu = ["Átváltás", "Feladatsorok", "Komplementerképzés", "Bináris műveletek", "Hálózat IP adatok" ,"Huffman" ,"Beállítások", "Segítség", "Kilépés"]
    functionMenu = [convertingNumbers, exercises, complementer, binaryOperations, networkCheck, huffman, settings, help]

    answer = 0
    while(answer != -1):
        os.system("clear")

        if(platform == "linux" or platform == "linux2"):
            width = os.get_terminal_size().columns
            middleText = "BinOp\n"
            os.system("setterm -foreground blue")
            print("Python 3.8.6", end="")
            print(middleText.center(width-len(middleText)))
            os.system("setterm -foreground white")
        elif(platform == "darwin" or platform == "win32"):
            width = os.get_terminal_size().columns
            middleText = "BinOp\n"
            print("Python 3.8.6", end="")
            print(middleText.center(width-len(middleText)))


        answer = md.draw(mainMenu)

        if(answer == -2 or answer == -3):
            input("  >> Nyomj entert a visszatéréshez! <<")
        elif(answer != -1):
            print(" >> " + mainMenu[answer] + " <<\n")
            functionMenu[answer]()
            input(" >> Kész <<")
        else:
            input(" >> A program most kilép <<")
            os.system("clear")

if(__name__ == "__main__"):
    main()
