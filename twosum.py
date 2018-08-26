"""
twosum.py

Given an array of integers, return indices of the two numbers such that
they add up to a specific target.
"""

def twosum(nums, target):
    """
    type nums: List[int]
    type target: int
    rtype: List[int]
    """
    differences = {}
    indices = []
    for i in range(len(nums)):
        n = nums[i]
        diff = target - n
        if n in differences:
            indices.append(differences[n])
            indices.append(i)
            break;
        else:
            differences[diff] = i

    return indices

print(twosum([1, 2], 3))

print(twosum([6, 2, 1, 7, 11, 15], 7))

print(twosum([2, 7, 11, 15], 9))

print(twosum([0, 4, 3, 0], 3))

print(twosum([-3,4,3,9], 0))
