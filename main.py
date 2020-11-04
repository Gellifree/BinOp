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
                
def separate(data):
    if(type(data) == str):
        result = []
        partOne = ""
        partTwo = ""
        i = 0
               


if(__name__ == "__main__"):
    main()
