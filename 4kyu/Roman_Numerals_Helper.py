class RomanNumerals:
    RN = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    RN2 = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    def highest_decimal_value(val):
        array = []
        for key,value in RomanNumerals.RN2.items():
            if value <= val:
                array.append(RomanNumerals.RN2[key])
        return RomanNumerals.RN[max(array)]

    def to_roman(val):
        roman_num = ''
        while val != 0:
            hdv = RomanNumerals.highest_decimal_value(val)
            roman_num += hdv
            val -= RomanNumerals.RN2[hdv]
        return roman_num

    def from_roman(roman_num):
        total = 0
        values = [RomanNumerals.RN2[x] for x in roman_num.upper()]
        for i in range(len(values) - 1):
            if values[i] >= values[i + 1]:
                total += values[i]
            else:
                total -= values[i]
        return total + values[-1]