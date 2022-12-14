class RomanNumeral():
    def __init__(self, roman):
        self.rom = roman

    def __int__(self):
        return RomanNumeral.to_numeral(self.rom)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.rom}')"

    def __str__(self):
        return self.rom

    def __add__(self, rnobj):
        return RomanNumeral.from_int(int(self) + int(rnobj))

    def __eq__(self, obj):
        return str(self) == obj if isinstance(obj, str) else int(self) == int(obj)

    def __lt__(self, rnobj):
        RomanNumeral.validate_instance(rnobj)
        return int(self) < int(rnobj)

    def __le__(self, rnobj):
        RomanNumeral.validate_instance(rnobj)
        return int(self) <= int(rnobj)

    def __gt__(self, rnobj):
        RomanNumeral.validate_instance(rnobj)
        return int(self) > int(rnobj)

    def __ge__(self, rnobj):
        RomanNumeral.validate_instance(rnobj)
        return int(self) >= int(rnobj)

    @classmethod
    def from_int(cls, ival):
        return cls(cls.to_roman(ival))

    @staticmethod
    def validate_instance(obj):
        if not isinstance(obj, (RomanNumeral, int)):
            raise TypeError
    
    @staticmethod
    def to_roman(ival):
        n2r = {1000:'M',900:'CM', 500:'D',400:'CD',100:'C',90:'XC',
               50:'L',40:'XL',10:'X', 9:'IX',5:'V',4:'IV',1:'I'}
        out = ''
        for n, r in n2r.items():
            out += r * int(ival / n)
            ival %= n
        return out

    @staticmethod
    def to_numeral(rval):
        r2n = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        return sum(-abs(r2n[ rval[i] ]) 
                   if len(rval) > i+1 and r2n[rval[i+1]] > r2n[rval[i]] else r2n[rval[i]]
                   for i in range(len(rval)) )
