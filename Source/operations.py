import normalizer, converter

nm = normalizer.Normalizer()
cnt = converter.Converter()

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

    def __slicer(self, string, mark):
        result = []
        slice = ""
        for char in string:
            if(char == mark):
                result.append(slice)
                slice = ""
            else:
                slice += char
        result.append(slice)
        return result

    def ipJoiner(self, ipList):
        joinedIp = ""
        for slice in ipList:
            joinedIp += str(slice) + "."
        joinedIp = joinedIp[:-1]
        return joinedIp


    def ipDatas(self, ip):
        network = {}
        ipSlices = self.__slicer(ip, ".")

        network["ip"] = self.ipJoiner(ipSlices)

        ipSlices[3] = str(int(ipSlices[3]) + 1)
        network["gateway"] = self.ipJoiner(ipSlices)

        ipSlices[3] = "255"
        network["broadcast"] = self.ipJoiner(ipSlices)
        ipSlices = self.__slicer(network["ip"], ".")
        ipSlices[3] = str(int(ipSlices[3]) + 2)
        network["devices"] = self.ipJoiner(ipSlices) + "-254"
        return network

    def ipNetwork(self, mask, ip):
        network = []
        ipSlices = self.__slicer(ip, ".")
        maskSlices = self.__slicer(mask, ".")

        binaryIp = []
        binaryMask = []

        for ip in ipSlices:
            binaryIp.append(cnt.convertFromTen(int(ip), 2, 5, False))
        binaryIp = nm.listNormalizer(binaryIp)
        for mask in maskSlices:
            binaryMask.append(cnt.convertFromTen(int(mask), 2, 5, False))
        binaryMask = nm.listNormalizer(binaryMask)

        for i in range(len(binaryIp)):
            network.append(self.binaryAnd(binaryIp[i], binaryMask[i]))

        s_network = []
        for slice in network:
            s_network.append(cnt.convertToTen(slice, 2, False))

        network = ""
        for slice in s_network:
            network += str(slice) + "."
        network = network[:-1]
        return network
