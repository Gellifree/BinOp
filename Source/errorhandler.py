class ErrorHandler():
    def isItBinary(self, number):
        for bit in number:
            if(bit != "0" and bit != "1"):
                return -1
        else:
            return 0
