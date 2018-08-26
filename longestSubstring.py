"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", which the length is 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

A sliding window is an abstract concept commonly used in array/string problems.
A window is a range of elements in the array/string which usually defined by the
start and end indices, i.e. [i,j)[i, j)[i,j) (left-closed, right-open). A sliding
window is a window "slides" its two boundaries to the certain direction. For example,
if we slide [i,j)[i, j)[i,j) to the right by 111 element, then it becomes
[i+1,j+1)[i+1, j+1)[i+1,j+1) (left-closed, right-open).
"""
def lengthOfLongestSubstring(s):
    letters = {}

    longest = 0
    i = 0
    j = 0

    for j in range(len(s)):
        c = s[j]

        if (c in letters):
            # lets i jump over the repeating character
            i = max(i, letters[c])

        longest = max(longest, j - i + 1)
        # dont remove c from hash, just update its value
        letters[c] = j + 1

    return longest

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkep"))
