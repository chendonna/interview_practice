"""
mergeSort.py

"""

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


def mergeSort(l1):
    if not l1:
        return []

    i = len(l1)
    if i == 1:
        return l1

    j = int(i/2)
    return mergeTwoLists(mergeSort(l1[:j]), mergeSort(l1[j:]))

print(mergeSort([2, 1]))
print(mergeSort([2, 1, 3]))
print(mergeSort([2, 1, 3, 0, 10, 5, 7, 6]))

"""
js version

function merge(arr, l, m, r) {
  var l1 = arr.slice(l, m+1);
  var l2 = arr.slice(m+1, r+1);

  var i = 0;
  var j = 0;
  var k = l;

  while ((i != l1.length) && (j != l2.length)){

    if (l1[i] < l2[j]) {
      arr[k] = l1[i];
      i++;
    } else {
      arr[k] = l2[j]
      j++;
    }
    k++;
  }

  /* adding the remaining elements of l1 to arr*/
  while (i != l1.length) {
    arr[k] = l1[i];
    k++;
    i++;
  }

  /* adding remaining elements to l2 to arr */
  while (j != l2.length) {
    arr[k] = l2[j];
    k++;
    j++;
  }

}

function mergeSort(roster, l, r) {
  if (l < r) {
    var m = Math.floor((l + r)/2)
    mergeSort(roster, l, m)
    mergeSort(roster, m+1, r)
    merge(roster, l, m, r)
  }



}

var arr = [2, 1, 4, 10, 8, 9, 7, 3, 1]
mergeSort(arr, 0, arr.length - 1);
console.log(arr)





"""
