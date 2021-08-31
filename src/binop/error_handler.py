class ErrorHandler():
    def valid_class(self, className):
        if(className != "A" and className != "a" and className != "B" and className != "b" and className != "C" and className != "c"):
            return -1
        return 0

    def binary(self, number):
        for bit in number:
            if(bit != "0" and bit != "1"):
                return -1
        else:
            return 0

    def is_number(self, number):
        for num in number:
            if(num != "0" and num != "1" and num != "2" and num != "3" and num != "4" and num != "5" and num != "6" and num != "7" and num != "8" and num != "9"):
                return -1
            else:
                return 0

    def valid_ip(self, number):
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
                if(self.is_number(slice) == -1):
                    return -2 #Az ip megfelelő felosztású, de nem számokat tartalmaz
                if(slice == ""):
                    return -4 #Üres slice rész
            for slice in ipSlices:
                if(int(slice) > 255):
                    return -3 #Az ip-ben nagyobb számok vannak, mint lehetne

            return 0 #Az Ip valid
        else:
            return -1 #Az Ip nem megfelelő felosztású
