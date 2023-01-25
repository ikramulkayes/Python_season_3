class Converter():
    @staticmethod
    def to_ascii(h):
        pass
    @staticmethod
    def to_hex(s):
        sum1 = ""
        for elm in s:
            elm = ord(elm)
            hexelm = '{0:x}'.format(elm)
            print(hexelm)
            return None


print((Converter.to_hex((45)))
