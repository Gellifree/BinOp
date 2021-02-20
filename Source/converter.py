class Converter():
    def readBackwards(self, data):
        result = ""
        i = len(data)-1
        while(i >= 0):
            result += data[i]
            i -= 1
        return result

    # data separate:
    def separate(self, data):
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

    def checkIfFractionExist(self, number):
        number = str(number)
        for i in range(len(number)):
            if(number[i] == "."):
                return True
        return False

    def safetyConvert(self, data):
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
    def integerCalculation(self, number, target, drawed):
        result = ""
        if(drawed == False):
            while(number >= 1):
                result += self.safetyConvert(int(number % target))
                number /= target
            return self.readBackwards(result)
        else:
            print("\n  Egészrész kiszámolása\n")
            print("  {} % {}".format(number, target))
            print("  =====")
            while(number >= 1):
                result += self.safetyConvert(int(number % target))
                print("  {} | {}".format(int(number/target), int(number % target)))
                number /= target
            print("  Egészrész: ", self.readBackwards(result),"\n")
            return self.readBackwards(result)

    def fractionCalculation(self, number, target, precision, drawed):
        result = ""
        if(drawed == False):
            i = 0
            while(i < precision):
                result += self.safetyConvert(self.separate(number*target)[0])
                number = self.separate(number * target)[1]
                i += 1
            return result
        else:
            i = 0
            print("\n  Törtrész kiszámolása\n")
            print("  {} * {}".format(number, target))
            print("  =======")
            while(i < precision):
                print("  {} * {} =>".format(number * target, target))
                result += self.safetyConvert(self.separate(number*target)[0])
                number = self.separate(number * target)[1]
                i += 1
            print("  Törtrész: ", result,"\n")
            return result

    def convertFromTen(self, number, target, precision, drawed):
        if(self.checkIfFractionExist(number) == True):
            result = ""
            result += self.integerCalculation(self.separate(number)[0], target, drawed)
            if(result == ""):
                result = "0"
            result += "."
            result += self.fractionCalculation(self.separate(number)[1], target, precision, drawed)
            return result
        else:
            result = ""
            result += self.integerCalculation(number, target, drawed)
            if(result == ""):
                result = "0"
            return result

    def integerCalculation_N(self, number, base, drawed):
        result = 0
        if(drawed == False):
            numberBack = self.readBackwards(number)
            i = 0
            while(i < len(numberBack)):
                result += (base**i) * self.safetyConvert(numberBack[i])
                i += 1
            return result
        else:
            numberBack = self.readBackwards(number)
            i = 0
            print("\n  Számítások elvégzése\n")
            while(i < len(numberBack)):
                print("  ({0}^{1}) * {2} = {3}".format(base,i,self.safetyConvert(numberBack[i]), (base**i)*self.safetyConvert(numberBack[i])))
                result += (base**i) * self.safetyConvert(numberBack[i])
                i += 1
            print("  Az egészrész: ", result,"\n")
            return result

    def fractionCalculation_N(self, number, base, drawed):
        result = 0
        if(drawed == False):
            i = 0
            while (i < len(number)):
                result += (base**(-(i+1))) * self.safetyConvert(number[i])
                i += 1
            return result
        else:
            print("  Törtrész számítása\n")
            i = 0
            while (i < len(number)):
                print("  ({0}^({1})) * {2} = {3}".format(base, -(i+1), self.safetyConvert(number[i]), (base**(-(i+1)))*self.safetyConvert(number[i])))
                result += (base**(-(i+1)))*self.safetyConvert(number[i])
                i += 1
            print("  A törtrész: ", result,"\n")
            return result

    def convertToTen(self, number, base, drawed):
        result = 0
        if(self.checkIfFractionExist(number) == True):
            partOne = self.separate(number)[0]
            partTwo = self.separate(number)[1]

            result = self.integerCalculation_N(partOne, base, drawed)
            result += self.fractionCalculation_N(partTwo, base, drawed)
            return result
        else:
            result = self.integerCalculation_N(number, base, drawed)
            return result
