def mergeSort(arr):
    """```
Description:
    Sorts an array using the merge sort algorithm.
Arguments:
    arr (list): The array to be sorted.
Response:
    list: The sorted array.
```"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    return merge(sortedLeft, sortedRight)


def merge(left, right):
    """```
Description:
     Merges two sorted lists into a single sorted list.
Arguments:
    left (list): The first sorted list.
    right (list): The second sorted list.
Response:
    list: A new sorted list containing elements from both input lists.
```"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print('Sorted array:', sortedArr)
