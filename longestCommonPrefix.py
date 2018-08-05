"""
    longestCommonPrefix.py
    finds the longest common prefix string amongst an array of strings

    Input: ["flower","flow","flight"]
    Output: "fl"

    Input: ["dog","racecar","car"]
    Output: ""

"""

def longestCommonPrefix(strs):
    """
    type strs: list[str]
    rtype: str
    """

    if not strs: # check if list is empty
        return ""

    prefix = min(strs, key = len)

    for s in strs:
        if s != prefix:
            new_prefix = ""
            for i in range(len(prefix)):
                if s[i] == prefix[i]:
                    new_prefix = new_prefix + s[i]
                else:
                    break;
            prefix = new_prefix

    return prefix
print(longestCommonPrefix([]))
print(longestCommonPrefix(["flower"]))
print(longestCommonPrefix(["flower", "flow"]))
print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racer", "car"]))
print(longestCommonPrefix(["car", "cot", "cunt"]))
