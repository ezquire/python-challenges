#Created by Tyler Gearing

class convert:
    def roman_to_arabic(self, s: str) -> int:
        numerals = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        arabic = 0
        for i in range(0, len(s) - 1):
            if(numerals[s[i]] < numerals[s[i + 1]]):
                arabic -= numerals[s[i]]
            else:
                arabic += numerals[s[i]]
        arabic += numerals[s[-1]]
        return arabic

print(convert().roman_to_arabic('MDCCLXXVI'))
