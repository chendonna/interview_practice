def checkRow(row, phrase):
    inRow = True
    # checked if the characters of the phrase are in the row
    for c in phrase:
        if c not in row: #if not in a row, return false
            inRow = False
            break # no longer necessary to continue looping through entire phrase
    return inRow

# time complexity: n: #number of phrases, O(n)
# make better: use strings instead of hash table -> save space but not time
# -> made the strings all lowercase first, save as seperate string (keep original)
# - c in phrase
def checkWords(phrases):
    # created a dict for every row
     row1 = {'q':1, 'Q':1, 'w':1, 'W':1, 'e':1, 'E':1, 'r':1, 'R': 1, 't':1, 'T':1, 'y':1, 'Y':1, 'u':1, 'U': 1,
             'i':1, 'I':1, 'o':1, 'O':1, 'p':1, 'P':1}
     row2 = {'a':1, 'A':1, 's':1, 'S':1, 'd':1, 'D':1, 'f':1, 'F':1, 'g':1, 'G':1, 'h':1, 'H':1, 'j':1, 'J':1, 'k':1,
             'K':1, 'l':1, 'L':1}
     row3 = {'z':1, 'Z':1, 'x':1, 'X':1, 'c':1, 'C':1, 'v':1, 'V':1, 'b':1, 'B':1, 'n':1, 'N':1,'m':1, 'M':1}
     res = []
     for phrase in phrases:
        # individually check each row and append the phrase to the response list if all the characters in
        # in the phrase is composed on the characters in a row
        if checkRow(row1, phrase):
            res.append(phrase)
        elif checkRow(row2, phrase):
            res.append(phrase)
        elif checkRow(row3, phrase):
            res.append(phrase)

     return res


print(checkWords(["alabama", "tree", "alaska", "nope"]))
