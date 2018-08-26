"""

"""
def checkAnagram(s1, s2):
    letters = [0] * 26
    i = 0
    for i in range(len(s1)):
        pos1 = ord(s1[i]) - ord('a')
        pos2 = ord(s2[i]) - ord('a')

        letters[pos1] = letters[pos1] + 1
        letters[pos2] = letters[pos2] - 1

    for n in letters:
        if n != 0:
            return False

    return True

def sherlockAndAnagrams(s):

    numAnagrams = 0
    strLength = 1
    lenS = len(s)

    while (strLength < lenS):
        for i in range(0, lenS - strLength):
            first = s[i:(i+strLength)]
            for j in range(i + 1, lenS - strLength +1):
                second = s[j:(j + strLength)]
                if checkAnagram(first, second):
                    numAnagrams = numAnagrams + 1

        strLength = strLength + 1

    return numAnagrams

print(sherlockAndAnagrams('abba'))
print(sherlockAndAnagrams('ifailuhkqq'))
print(sherlockAndAnagrams('kkkk'))
print(sherlockAndAnagrams('abcd'))
print(sherlockAndAnagrams('cdcd'))
print(sherlockAndAnagrams(''))
print(sherlockAndAnagrams('ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel'))
print(sherlockAndAnagrams('gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde'))
