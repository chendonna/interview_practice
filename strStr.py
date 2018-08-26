"""
    find index of starting needle

    ex. haystack = "hello" needle = "ll"
        output: 2
"""
def strStr(haystack, needle):
    """
    type haystack: str
    type needle: str
    type return: int
    """
    len_haystack = len(haystack)
    len_needle = len(needle)
    if len_needle == 0: return 0 # edge case: needle is empty
    if len_needle > len_haystack: #edge case
        return -1

    ind_h = 0
    ind_n = 0

    while (ind_h < len_haystack):
        if haystack[ind_h] == needle[ind_n]:
            ind_n = ind_n + 1
            ind_h = ind_h + 1
            # once all of the needle has been found, return
            if ind_n == len_needle:
                return (abs(ind_h - len_needle))
        else:
            # ind_h must go back to starting position but + 1
            if ind_n > 0:
                ind_h = abs(ind_h - ind_n) + 1
            else:
                ind_h = ind_h + 1
            ind_n = 0
    return -1


print(strStr("halla", "la"))
print(strStr("aaa", "a"))
print(strStr("mississippi", "issipi"))
