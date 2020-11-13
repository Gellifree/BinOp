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
        print("  {0} % {1}".format(number, target))
        print("  =====")
        while(number >= 1):
            result += safetyConvert(int(number % target))
            print("  {0} | {1}".format(int(number/target), int(number % target)))
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
        print("\n  Törtrész kiszámolása")
        print("  {0} * {1}".format(number, target))
        print("  =======")
        while(i < precision):
            print("  {0} * {1} =>".format(number * target, target))
            result += safetyConvert(separate(number*target)[0])
            number = separate(number * target)[1]
            i += 1
        print("  Törtrész: ", result,"\n")
        return result



#Use these to check if the functions works
def first():
    fractionCalculation(0.75,2,5,True)
    pass

def second():
    integerCalculation(8,2,True)
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
