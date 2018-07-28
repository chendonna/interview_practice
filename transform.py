# input: [1 2 3 4 5 6 7 8]
# output: [1 5 3 7 2 6 4 8]
"""
1 2 3 4 | 5 6 7 8
1 2 | 3 4
1 | 2
1 2 | 3 4
1 3 2 4 | 5 7 6 8

"""
# 1 | 2
# 5 | 6
# 3 | 4
# 7 | 8

"""
1, 2, 3, 4
1, 2 | 3, 4

1, 3, 2, 4
"""

# time: nlogn -> logn to split in half and n to merge each time

# merges the two lists, arr1 and arr2 together and creates a new list that has the elements from both in
# alternating order
def merge (arr1, arr2):
    len_both = len(arr1) + len(arr2)
    merged = []
    for i in range(len_both):
        index = int(i/2) # calculates the correct index for the next elements in both lists
        # alterates which list gets appended to the new merged list
        if (i%2) == 0: #if even, append the next element from the first list
            merged.append(arr1[index])
        else: #if odd, append the next element from the second list
            merged.append(arr2[index])
    return merged

# recursively splits the array in half and then merges each half of the two lists together
def  transform(array):
    len_array = len(array)
    if len_array == 1: #base case, when the length of array is 1, return the array
        return array
    split = int(len_array/2) #finds the index to split the array in
    left = transform(array[:split])
    right = transform(array[split:])

    return merge(left, right) #returns the merged lists

print (transform([1, 2, 3, 4]))
