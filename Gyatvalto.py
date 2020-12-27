def gen_00(binary_string,X):

    elvalaszto_01=','
    elvalaszto_02='.'
    elem_01=""
    elem_02=""
    talalat=0
    eredmeny=""
    for x in binary_string:
        if x ==elvalaszto_01 or x ==elvalaszto_02:
            talalat=1
        else:
            if talalat==0:
                elem_01 = elem_01 + x
            elif talalat==1:
                elem_02 = elem_02 + x
    #print(elem_01,elem_02)
    if elem_01 != "":
        decimal_representation = int(elem_01, 2)
        if(X==16):
            hexadecimal_string = hex(decimal_representation)
            #print (hexadecimal_string)
            eredmeny =eredmeny + hexadecimal_string[2:]
        elif(X==8):
            octal_string = oct(decimal_representation)
           # print (octal_string)
            eredmeny = eredmeny + octal_string[2:]
    if elem_02 != "":
        eredmeny = eredmeny + ","
        decimal_representation = int(elem_02, 2)
        if (X == 16):
            hexadecimal_string = hex(decimal_representation)
            #print(hexadecimal_string)
            eredmeny = eredmeny + hexadecimal_string[2:]
        elif (X == 8):
            octal_string = oct(decimal_representation)
            #print(octal_string)
            eredmeny = eredmeny + octal_string[2:]
    else:
        print("")
    print(eredmeny)

gen_00 ("01001,01",8)
gen_00 ("01001",8)
gen_00 ("0,01",8)