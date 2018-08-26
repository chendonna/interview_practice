"""

"""

def isPalindrome (x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    temp = x
    reversed = 0
    while temp > 0:
        reversed = reversed * 10 + temp % 10
        temp = int(temp/10)

    return (x == reversed)

print(isPalindrome(134565431))
