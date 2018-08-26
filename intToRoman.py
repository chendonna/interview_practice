"""
"""

def intToRoman(num):
    #when iterating through dict, has to be in this order
    dict = {1000:'M', 900: 'CM',500: 'D',400: 'CD',100: 'C',90:'XC',
    50: 'L',40: 'XL',10: 'X',9:'IX',5: 'V',4:'IV',1: 'I'}

    str = ""
    for key in dict:
        x = int(num/key)
        num = num % key # iterate on the mod
        str += x * dict[key] #makes x number of copies of the new c

    return str

print(intToRoman(3))
print(intToRoman(4))
print(intToRoman(5))
print(intToRoman(9))
print(intToRoman(10))
print(intToRoman(59))
print(intToRoman(1994))
print(intToRoman(2154))
