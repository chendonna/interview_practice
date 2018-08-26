"""
valid parentheses
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    lenS = len(s)
    stack = []
    dict = {')': '(', '}': '{', ']':'['}
    for c in s:
        if c in dict.values():
            stack.append(c)
        else:
            if stack == []:
                return False
            if dict[c] != stack.pop():
                return False

    return stack == []

print(isValid(''))
print(isValid(']'))
print(isValid('(])'))

print(isValid('(){}[]'))
print(isValid('({[()]})'))
print(isValid('({[(}]})'))
