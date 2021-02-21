import normalizer

nm = normalizer.Normalizer()

class Operator():
    def binaryAnd(self, a, b):
        result = ""
        list = nm.listNormalizer([a,b])
        for i in range(len(list[0])):
            if(list[0][i] + list[1][i] == "11"):
                result += "1"
            else:
                result += "0"
        return result


    def binaryOr(self, a, b):
        result = ""
        list = nm.listNormalizer([a,b])
        for i in range(len(list[0])):
            if(list[0][i] == "0" and list[1][i] == "0"):
                result += "0"
            else:
                result += "1"
        return result

    def binaryAdd(self, a, b):
        pass

    def binarySub(self, a, b):
        pass
