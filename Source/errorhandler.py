class ErrorHandler():
    def isItBinary(self, number):
        for bit in number:
            if(bit != "0" and bit != "1"):
                return -1
        else:
            return 0

    def isItNumber(self, number):
        for num in number:
            if(num != "0" and num != "1" and num != "2" and num != "3" and num != "4" and num != "5" and num != "6" and num != "7" and num != "8" and num != "9"):
                return -1
            else:
                return 0

    def isItValidIP(self, number):
        dotSum = 0
        for bit in number:
            if(bit == "."):
                dotSum += 1
        if(dotSum == 3):
            ipSlices = []
            slice = ""
            for i in range(len(number)):
                if(number[i] == "."):
                    ipSlices.append(slice)
                    slice = ""
                else:
                    slice += number[i]
            ipSlices.append(slice)

            for slice in ipSlices:
                if(self.isItNumber(slice) == -1):
                    return -2 #Az ip megfelelő felosztású, de nem számokat tartalmaz

            for slice in ipSlices:
                if(int(slice) > 255):
                    return -3 #Az ip-ben nagyobb számok vannak, mint lehetne

            return 0 #Az Ip valid
        else:
            return -1 #Az Ip nem megfelelő felosztású
