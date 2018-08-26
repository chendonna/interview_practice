"""
reverse.py
"""
MAX_INT = (2**31) - 1
MIN_INT = -2**31
def reverse(x):

    res = 0

    while x != 0:
        first = x % 10
        print(first)
        res = res * 10 + first
        if res > MAX_INT or res < MIN_INT:
            return 0
        x = int(x/10)

    return res

print(reverse(123))
print(reverse(-1234))
print(reverse(10))
print(reverse(-10))

"""
if x > 0:
    res = (res * 10) + first
else:
    res = (res*10) - (10 - first)
"""
