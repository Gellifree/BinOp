import converter

cnt = converter.Converter()

class Normalizer():
    def normalizeSingle(self, string, size):
        result = ""
        zeroes = ""
        for i in range(size - len(string)):
            zeroes += "0"
        result = zeroes + string
        return result


    def listNormalizer(self, list):
        result = []
        maxSize = len(max(list, key = len))
        for item in list:
            result.append(self.normalizeSingle(item, maxSize))
        return result
