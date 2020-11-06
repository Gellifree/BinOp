#importing needed resources
import os

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
def readBackwards():
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


def first():
    pass

def second():
    pass

def main():
    mainMenu = ["Első menüpont", "Második menüpont", "Kilépés"]
    executableMenu = ["first()", "second()"]

    menuState = 0
    answer = 0
    while(answer != "q" and answer != "Q"):
        os.system("clear")
        print("Számrendszer átváltó és feladatgeneráló")

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
