import os

from binop import fast_converter
from binop import converter

cnt = converter.Converter()

numberBases = [2,2,8,8,16,16,2,8,16,8,16]
def solve_exercises(exercises):
    baseIndex = 0
    os.system("clear")
    for exercise in exercises:
        for number in exercise:
            print("  Átváltandó szám:", number, "\n")
            if(baseIndex < 6):
                print("   Az eredmény:",cnt.convert_to_ten(number,numberBases[baseIndex],True))
                input("  >> Üss entert a következő feladat megjelenítéséhez. <<")
                os.system("clear")
                baseIndex += 1
            elif(baseIndex == 9):
                print("  Nyolcasban:", end="")
                print("   " + fastConvert.convert(number,8))
                print("  Tizenhatban:", end="")
                print("   " + fastConvert.convert(number, 16))
            else:
                print("   Az eredmény:", cnt.convert_from_ten(float(number), numberBases[baseIndex], 5, True))
                input("  >> Üss entert a következő feladat megjelenítéséhez. <<")
                os.system("clear")
                baseIndex += 1
