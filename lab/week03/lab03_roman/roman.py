def roman(numerals):
    '''
    Given Roman numerals as a string, return their value as an integer. You may
    assume the Roman numerals are in the "standard" form, i.e. any digits
    involving 4 and 9 will always appear in the subtractive form.

    For example:
    >>> roman("II")
    2
    >>> roman("IV")
    4
    >>> roman("IX")
    9
    >>> roman("XIX")
    19
    >>> roman("XX")
    20
    >>> roman("MDCCLXXVI")
    1776
    >>> roman("MMXIX")
    2019
    '''
    value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    result = 0
    for roman_letter in range(len(numerals) - 1):
        if value[numerals[roman_letter]] < value[numerals[roman_letter + 1]]:
            result -= value[numerals[roman_letter]]
        else:
            result += value[numerals[roman_letter]]
    result += value[numerals[-1]]
    return result
#print(roman('XIX'))
