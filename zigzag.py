"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
"""
def zigzag(s, numRows):
    if s == "":
        return ""
    new_str = ""
    # length till the next character in the row
    cycleLen = 2*numRows - 2
    n = len(s)
    for i in range(numRows):
        for j in range(i, n, cycleLen):
            new_str += s[j]
            # finds the index of the c in the diagonals based off row
            diagonal = j + cycleLen - 2*i
            # first and last rows dont have diagonals
            if (i != 0 and i != numRows - 1 and diagonal < n):
                new_str += s[diagonal]

    return new_str

print(zigzag("PAYPALISHIRING", 4))
print(zigzag("PAYPALISHIRING", 5))
