from binop import normalizer
from binop import converter

nm = normalizer.Normalizer()
cnt = converter.Converter()

class Operator():
    def binary_and(self, a, b):
        result = ""
        list = nm.list_normalizer([a,b])
        for i in range(len(list[0])):
            if(list[0][i] + list[1][i] == "11"):
                result += "1"
            else:
                result += "0"
        return result


    def binary_or(self, a, b):
        result = ""
        list = nm.list_normalizer([a,b])
        for i in range(len(list[0])):
            if(list[0][i] == "0" and list[1][i] == "0"):
                result += "0"
            else:
                result += "1"
        return result

    def binary_add(self, a, b):
        pass

    def binary_sub(self, a, b):
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

    def ip_joiner(self, ipList):
        joinedIp = ""
        for slice in ipList:
            joinedIp += str(slice) + "."
        joinedIp = joinedIp[:-1]
        return joinedIp


    def ip_datas(self, ip):
        network = {}
        ipSlices = self.__slicer(ip, ".")

        network["ip"] = self.ip_joiner(ipSlices)

        ipSlices[3] = str(int(ipSlices[3]) + 1)
        network["gateway"] = self.ip_joiner(ipSlices)

        ipSlices[3] = "255"
        network["broadcast"] = self.ip_joiner(ipSlices)
        ipSlices = self.__slicer(network["ip"], ".")
        ipSlices[3] = str(int(ipSlices[3]) + 2)
        network["devices"] = self.ip_joiner(ipSlices) + "-254"
        return network

    def ip_in_binary(self, ip):
        ipSlices = self.__slicer(ip, ".")
        binaryIp = []
        for ip in ipSlices:
            binaryIp.append(cnt.convert_from_ten(int(ip), 2, 5, False))
        # binaryIp = nm.list_normalizer(binaryIp) #Ha akarjuk normalizálni
        return self.ip_joiner(binaryIp)

    def ip_network(self, mask, ip):
        network = []
        ipSlices = self.__slicer(ip, ".")
        maskSlices = self.__slicer(mask, ".")

        binaryIp = []
        binaryMask = []

        for ip in ipSlices:
            binaryIp.append(cnt.convert_from_ten(int(ip), 2, 5, False))
        binaryIp = nm.list_normalizer(binaryIp)
        for mask in maskSlices:
            binaryMask.append(cnt.convert_from_ten(int(mask), 2, 5, False))
        binaryMask = nm.list_normalizer(binaryMask)

        for i in range(len(binaryIp)):
            network.append(self.binary_and(binaryIp[i], binaryMask[i]))

        s_network = []
        for slice in network:
            s_network.append(cnt.convert_to_ten(slice, 2, False))

        network = ""
        for slice in s_network:
            network += str(slice) + "."
        network = network[:-1]
        return network
