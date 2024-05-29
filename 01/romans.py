def roman_to_int():
    roman = input("Insira seu número em algarismos romanos: ")

    nums = {'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1}

    roman = roman.upper()
    total = 0
    for i in range(len(roman)):
        try:
            value = nums[roman[i]]
            if i + 1 < len(roman) and nums[roman[i + 1]] > value:
                total -= value
            else:
                total += value
        except KeyError:
            raise ValueError('Input is not a valid Roman numeral: %s' % roman)

    return total

print(roman_to_int())


def int_to_roman(input):
    if not isinstance(input, type(1)):
        raise TypeError, "expected integer, got %s" % type(input)
    if not 0 < input < 4000:
        raise ValueError, "Argument must be between 1 and 3999"
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = []

for i in range(len(ints)):
    count = int(input / ints[i])
    result.append(nums[i] * count)
    input -= ints[i] * count
return ''.join(result)
