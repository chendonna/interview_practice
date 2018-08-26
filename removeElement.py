"""
removeELement.py
Given an array nums and a value val, remove all instances of that value in-place
and return the new length.
"""

def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    n = len(nums)
    i = 0
    while (i < n):
        if nums[i] == val:
            n = n-1
            nums.remove(val)
        else:
            i = i+1

    return n
