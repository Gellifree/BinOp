import main, Gyatvalto


numberBases = [2,2,8,8,16,16,2,8,16,8,16]
def solveExercises(exercises):
    baseIndex = 0
    for exercise in exercises:
        for number in exercise:
            print("  Átváltandó szám:", number)
            if(baseIndex < 6):
                main.convertToTen(number,numberBases[baseIndex],True)
                input("  >> Üss entert a következő feladat megjelenítéséhez. <<")
                baseIndex += 1
            elif(baseIndex == 9):
                print("  Nyolcasban:")
                print("   " + Gyatvalto.gen_00(number, 8))
                print("  Tizenhatba:")
                print(Gyatvalto.gen_00(number, 16))
            else:
                main.convertFromTen(float(number), numberBases[baseIndex], 5, True)
                input("  >> Üss entert a következő feladat megjelenítéséhez. <<")
                baseIndex += 1
