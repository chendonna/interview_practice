import sys
"""
We say that a string, , contains the word hackerrank if a
subsequence of the characters in  spell the word hackerrank.
For example, haacckkerrannkk does contain hackerrank, but
haacckkerannk does not (the characters all appear in the same
order, but it's missing a second r).
"""


def subseq (s):
    hr = "hackerrank"
    len_hr = len(hr)
    j = 0
    for i in s:
        if hr[j] == i:
            j += 1
        if j == (len(hr)):
            return "YES"

    return "NO"



q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    print(subseq(s))
