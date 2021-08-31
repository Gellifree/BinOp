from binop import converter

cnt = converter.Converter()

def convert(number, target):
    result = ""
    fractioned = False

    if(cnt.fraction_exist(number) == True):
        fractioned = True

    size = 0
    if(target == 8):
        size = 3
    elif(target == 16):
        size = 4

    if(fractioned):
        #Szeparáljuk el az egészrészt a törtrésztől
        integer = cnt.separate(number)[0]
        fraction = cnt.separate(number)[1]

        #Mivel a végére kell beszúrni a nullákat, fordítsuk meg
        integer = cnt.read_backwards(integer)

        #Amennyiben nem osztható hárommal-néggyel, pótolnunk kell:
        if(len(integer) % size != 0):
            numberOfZeroes = size - (len(integer) % size) #Ennyi nulla hiányzik hogy osztható legyen
            for zero in range(numberOfZeroes):
                integer += "0"
        integer = cnt.read_backwards(integer) #Fűzzük hozzá a nullákat, majd fordítsuk vissza


        #Ugyan ez a tört részre, kivéve hogy itt, nem szabad megfordítani
        if(len(fraction) % size != 0):
            numberOfZeroes = size - (len(fraction) % size)
            for zero in range(numberOfZeroes):
                fraction += "0"

        #Kipótoltuk annyi nullával, hogy mindent kényelmesen hármas-négyes részekre osszunk
        counter = 0
        part = ""
        result = ""
        for i in range(len(integer)):
            if(counter == size):
                result += cnt.safety_convert(cnt.convert_to_ten(part, 2, False))
                #A safety_convert segítségével, a 16-os átváltásnál biztosítjuk a hibamentes működést
                part = ""
                counter = 0
            part += integer[i]
            counter += 1
        result += cnt.safety_convert(cnt.convert_to_ten(part, 2, False)) + "."
        part = ""
        counter = 0

        for i in range(len(fraction)):
            if(counter == size):
                result += cnt.safety_convert(cnt.convert_to_ten(part, 2, False))
                part = ""
                counter = 0
            part += fraction[i]
            counter += 1
        result += cnt.safety_convert(cnt.convert_to_ten(part, 2, False))
    else:
        integer = cnt.read_backwards(number)

        if(len(integer) % size != 0):
            numberOfZeroes = size - (len(integer) % size)
            for zero in range(numberOfZeroes):
                integer += "0"
        integer = cnt.read_backwards(integer)
        counter = 0
        part = ""
        result = ""
        for i in range(len(integer)):
            if(counter == size):
                result += cnt.safety_convert(cnt.convert_to_ten(part, 2, False))
                part = ""
                counter = 0
            part += integer[i]
            counter += 1
        result += cnt.safety_convert(cnt.convert_to_ten(part, 2, False))
    #print(result)
    return result


if(__name__ == "__main__"):
    convert("11111001", 16)
