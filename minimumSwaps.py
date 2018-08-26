"""
minimum swaps
"""

def minimumSwaps(arr):
    count = 0
    i = 0
    l = len(arr)
    sorted_arr = sorted(arr)

    while i < l:
        n = arr[i]
        pos = sorted_arr.index(n)
        if (i != pos):
            arr[i], arr[pos] = arr[pos], arr[i]
            count += 1
            i -= 1
        i += 1

    return count

print(minimumSwaps([4, 3, 1, 2]))
print(minimumSwaps([2, 3, 4, 1, 5]))
print(minimumSwaps([1, 3, 5, 2, 4, 6, 8]))
print(minimumSwaps([10, 4, 5, 3, 7]))
