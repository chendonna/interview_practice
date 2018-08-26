"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

to do this:
know that for ababa -> bab is already a palindrome so just need
to check the characters around it to see if they are the same, if the
same then they are a palindrome

check around the centers of the palindrome:
2n - 1 centers -> account for evens as well

ex. "babad" -> b, ba, a, ab, b, ba, a, ad, d

expand throughout these centers to find the palindrome

O(n^2) time complexity and O(1) space
"""
def checkAroundCenter(s, l, r):
    lenS = len(s)

    while (l >= 0 and r < lenS) and s[l] == s[r]:
        l -= 1
        r += 1

    return (r - l - 1)

def longestPalindrome(s):
    lenS = len(s)

    start = 0
    end = 0
    for i in range(lenS):
        len1 = checkAroundCenter(s, i, i)
        len2 = checkAroundCenter(s, i, i+1)

        max_len = max(len1, len2)
        if max_len > (end - start + 1):
            #max_len - 1 for the palindromes with even number of letters
            start = i - int((max_len - 1)/2)
            end = i + int(max_len/2)

    return s[start:(end + 1)]

print(checkAroundCenter("a", 0, 0))
print(checkAroundCenter("ab", 0, 1))
print(checkAroundCenter("aba", 1, 1))
print(longestPalindrome("a"))
print(longestPalindrome("ab"))
print(longestPalindrome("dbabc"))
print(longestPalindrome("abbac"))
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
