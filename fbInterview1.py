# fb phone interview 1 - donna

# input: list of pairs of integers, for example [(1,2), (5,6), (7,3), ...]
# input: a non-negative integer "K"
# output: the "K" points from the input that are closest to the origin (0,0)

# for example: if K=2, [(1,2), (7,3)]

# first solution that I thought of right off the bat
# time complexity: O(nlogn) because of the sorting
def k_from_origins(coords, k):
    lenC = len(coords)

    if lenC < k: #edge case: if k is greater than the elements in the list
        return None

    # list stores tuples of the calculated distance and the original index that
    # the point was located in as (dist, index)
    distances = []
    for i in range(lenC):
        (x, y) = coords[i]
        distance = sqrt(x^2 + y^2)
        distances.append((distance, i))

    """ what this is doing is sorting the distances array using only the
        distance calculated and not the index    """
    distances = sorted(distances, lambda (d, ind): d)

    ret = [] #creates an array of just the k elements
    for j in range(k):
        (d, ind) = distances[j]
        ret.append(coords[ind])

    return ret
"""
Interviewer then asks if there was a way for me to sort the coordinates
using lambda and im a motherfucking dumbass for not realizing earlier
because its like 2 lines of code lolol
"""
def k_from origin2(coords, k):
    """
    The lambda is a sort function given to sorted which is used on each
    each element in coords to calc their distance and the sorted will sort the array
    using the distances
    """
    coords = sorted(coords, lambda (x, y): sqrt(x^2 + y^2))
    return coords[:k] #returns first k

"""
Interviewer says what if k is really small, are you going to sort each
element in coords? At first I say you can use a min heap that has k elements
so you can keep track of the minimum k elements but get confused and change that
to an array. After being lost for like 10 minutes going in the wrong direction,
I get to the conclusion of using a maxHeap (thx fb dude for not telling me
I was going in the completely wrong direction)
max Heap: root will have the greatest element and all its children will be
          less than it
note: i didnt know the syntax for the heap class in python so I told him that
      and made up some random heap function names
"""
def k_from_origin(coords, k):
    maxHeap = maxHeap()

    #goes through the coordinate array and calculates the distance
    for i in range(len(coords)):
        (x, y) = coords[i]
        distance = sqrt(x^2 + y^2)
        # if the maxheap is not filled yet, insert the distance and index into it
        # this is kinda like the first method
        if maxHeap.size() < k:
            maxHeap.insert((distance, index))
        else:
            # compare the distance to the root of the max heap and if it is less
            # it add it to the head and remove the root (python function should
            # automatically keep the heap invariant)
            if distance < maxHeap.top():
                maxHeap.insert((distance, index))
                maxHeap.deleteMax()

    listHeap = list(maxHeap) #changes the heap into a list

    # then you can go through it again like in the first function and get the
    # k elements that are in the heap according the index (didnt write this out)

    return Li
