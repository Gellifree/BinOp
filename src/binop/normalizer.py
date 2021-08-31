from binop import converter


cnt = converter.Converter()

class Normalizer():
    def single_normalizer(self, string, size):
        result = ""
        zeroes = ""
        for i in range(size - len(string)):
            zeroes += "0"
        result = zeroes + string
        return result


    def list_normalizer(self, list):
        result = []
        maxSize = len(max(list, key = len))
        for item in list:
            result.append(self.single_normalizer(item, maxSize))
        return result
