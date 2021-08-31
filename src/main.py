#!/usr/bin/python3

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
from binop import error_handler
from binop import settings as st
import os

md = menu.MenuDrawer()
cnt = converter.Converter()
nm = normalizer.Normalizer()
op = operations.Operator()
err = error_handler.ErrorHandler()



def convertin_numbers():
    miniMenu = ["Átváltás tízes számrendszerből","Átváltás tízes számrendszerbe"]
    miniexec = [from_ten, to_ten]
    answer = md.draw(miniMenu)
    print(" >>", miniMenu[int(answer)], "<< ")
    miniexec[answer]()

def from_ten():
    print("  Add meg a számot, amit át szeretnél váltani!")
    number = input("  >> ")
    print("  Add meg a célszámrendszer alapját, amibe átszeretnéd váltani! [2-16]")
    #We could give the user a menu maybe
    target = int(input("  >> "))
    precision = 0
    if(cnt.fraction_exist(number) == True):
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


    print("\n  Az átváltás eredménye: ", cnt.convert_from_ten(number, target, precision, drawed))

def to_ten():
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
    print(" Az átváltás eredénye: ", cnt.convert_to_ten(number, target, drawed))

def exercises():
    miniMenu = ["Feladatsor generálása", "Feladatsorok megtekintése"]
    miniexec = [gen_excercise, look_excercise]

    answer = md.draw(miniMenu)
    print(" >>",miniMenu[answer], "<<")
    miniexec[answer]()

def gen_excercise():
    fileName = input("   >> Milyen néven kívánja elmenteni a feladatsort?: ")
    generate.save(fileName)
    print("   >> Fájl elmentve! <<")

def look_excercise():
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
        result = generate.draw_from_file(data)
    print("  Látni akarod a feladatsor megoldását? [Y/n]")
    solution = input("  >> ")
    if(solution == "y" or solution == "" or solution == "Y"):
        solver.solve_exercises(result)


def complementer():
    print(" Komplementerképzésért felelős menüpont")


def binary_and():
    print("  Bináris ÉS műveletért felelős menüpont")

    print("  Kérem adja meg az első számot: ")
    number1 = input("  >> ")
    if(err.binary(number1) == -1):
        print("  >> A bináris És műveletnek, csak bináris értékre van értelme! <<")
        #Később ciklusba szervezni
        return
    print("  Kérem adja meg a második számot: ")
    number2 = input("  >> ")
    if(err.binary(number2) == -1):
        print("  >> A bináris És műveletnek, csak bináris értékre van értelme! <<")
        return
    result = op.binary_and(number1, number2)
    print("\n  >> A logikai És eredménye: ", result)

def binary_or():
    print("  Bináris VAGY műveletért felelős menüpont")

def ip_check():
    print("  Két IP cím ellenőrzése:")
    print("\n  >> Add meg az Alhálózati maszkot: ")
    mask = input("  >> ")
    if(err.valid_ip(mask) < 0):
        print("  >> A megadott alhálózati maszk helytelen! <<")
        return
    print("\n  >> Add meg az feladó IP címét: ")
    ip1 = input("  >> ")
    if(err.valid_ip(ip1) < 0):
        print("  >> A megadott Ip helytelen! <<")
        return
    print("\n  >> Add meg a címzett IP címét: ")
    ip2 = input("  >> ")
    if(err.valid_ip(ip2) < 0):
        print("  >> A megadott Ip helytelen! <<")
        return

    print("  A két IP cím hálózata: \n")

    print("  >> Feladó:", op.ip_network(mask, ip1))

    print("\n  >> Címzett:", op.ip_network(mask, ip2))
    if(op.ip_network(mask, ip1) == op.ip_network(mask, ip2)):
        print("  >>> A hálózat megeggyezik <<<")


def binary_operations():
    binaryMenu = ["Bináris ÉS", "Bináris VAGY", "IP ellenőrzés"]
    functionMenu = [binary_and, binary_or, ip_check]

    answer = md.draw(binaryMenu)
    functionMenu[int(answer)]()

def network_check():
    print("  Add meg a hálózat Ip-jét: ")
    network = input("  >> ")
    if(err.valid_ip(network) < 0):
        print("  >>> A hálózati címben elírás történt! <<<")
    else:
        print("\n  Milyen címosztályban értelmezett? (A,B,C): ")
        class_asnwer = input("  >> ")
        if(err.valid_class(class_asnwer) == -1):
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
            print("  >> Binárisban: \t", op.ip_in_binary(result["ip"]))
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
    functionMenu = [convertin_numbers, exercises, complementer, binary_operations, network_check, huffman, settings, help]

    answer = 0
    while(answer != -1):
        os.system("clear")

        if(platform == "linux" or platform == "linux2"):
            width = os.get_terminal_size().columns
            middleText = "BinOp\n"
            os.system("setterm -foreground cyan")
            print("Python 3.9.5", end="")
            print(middleText.center(width-len(middleText)))
            os.system("setterm -foreground white")
        elif(platform == "darwin" or platform == "win32"):
            width = os.get_terminal_size().columns
            middleText = "BinOp\n"
            print("Python 3.9.5", end="")
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
