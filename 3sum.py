"""
3sum.py

Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.
"""
def twoSum(nums, target):
    indices = []
    differences = {}

    for i in range(len(nums)):
        n = nums[i]
        diff = target - n
        if n in differences:
            #(val, seen) = differences[n]
            #if not seen:
                #differences[n] = (n, True)
            indices.append([differences[n], n])
        else:
            differences[diff] = (n)

    return indices

# need to be able to handle duplicates fuckkkk
def threeSum (nums):

    if len(nums) < 3:
        return []

    solution = []
    nums.sort()
    print(nums)
    for i in range(len(nums)-1):
        indices = twoSum(nums[i+1:], -nums[i])
        print(indices)
        

    solution = []
    #for i in indices:
        #solution.append([nums[0]] + i)

    return solution

print(threeSum([-1, 0, 1, 2, -1, -4]))
#print(threeSum([0, 0, 0, 0]))
print(threeSum([3,0,-2,-1,1,2]))
