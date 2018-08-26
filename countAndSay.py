"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

"""
def countAndSay(n):

    s = "1"
    for i in range(1, n):
        count = 1
        new_s = ""
        j = 0
        for j in range(1, len(s)):
            if s[j-1] != s[j]:
                new_s = new_s + str(count) + s[j-1]
                count = 1
            else:
                count += 1

        # for the last digit not accounted for, add it to the new string
        new_s += str(count) + s[j]
        s = new_s


    return s

print(countAndSay(2))
print(countAndSay(3))
print(countAndSay(4))
print(countAndSay(5))
print(countAndSay(6))
print(countAndSay(7))
