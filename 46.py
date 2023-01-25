class Converter():
    @staticmethod
    def to_ascii(h):
        sum1 = ""
        lst = []
        prev = ""
        for elm in range(0,len(h)+1,2):
            if elm+1 < len(h):
                
                lst.append(h[elm]+h[elm+1])
        #print(lst)
        for elm in lst:
           # print(elm)
            dicelm = int(elm,16)
            
            sum1 += chr(dicelm)
        return sum1




    @staticmethod
    def to_hex(s):
        sum1 = ""
        for elm in s:
            elm = ord(elm)
            sum1 += '{0:x}'.format(elm)
            #print(hexelm)
        return sum1


print((Converter.to_hex(("Look mom, no hands"))))
print((Converter.to_ascii(("4c6f6f6b206d6f6d2c206e6f2068616e6473"))))