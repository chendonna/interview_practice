# merge two sorted lists

def mergeTwoLists(l1, l2):
    # if not l1 and not l2:
    #     return []

    i = 0
    j = 0
    newList = []
    while (i != len(l1)) and (j != len(l2)):
        if l1[i] < l2[j]:
            newList.append(l1[i])
            i = i + 1
        else:
            newList.append(l2[j])
            j = j + 1

    if i == len(l1):
        newList = newList + l2[j:]
    if j == len(l2):
        newList = newList + l1[i:]

    return newList


print(mergeTwoLists([], []))
print(mergeTwoLists([1], []))
print(mergeTwoLists([], [1]))
print(mergeTwoLists([1, 3], [2]))
print(mergeTwoLists([1, 2, 4], [1, 3, 4]))
print(mergeTwoLists([1, 3, 4, 4, 6, 8, 10], [7, 12]))
