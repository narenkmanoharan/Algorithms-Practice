import doctest
from random import randrange

def quicksort(lst, start, end):
    '''
    Returns a sorted list using quicksort

    >>> quicksort([10,12,523,123,45,562,241,47,768,435,567], 0, 10)
    [10, 12, 45, 47, 123, 241, 435, 523, 562, 567, 768]

    '''
    if start < end:
        pIndex = partition(lst, start, end)
        quicksort(lst, start, pIndex-1)
        quicksort(lst, pIndex+1, end)
    return lst

def partition(lst, start, end):
    '''
    Returns the pIndex
    '''
    pivot = lst[end]
    pIndex = start
    for i in range(start, end):
        if lst[i] < pivot:
            lst[pIndex], lst[i] = lst[i], lst[pIndex]
            pIndex += 1
    lst[pIndex], lst[end] = lst[end], lst[pIndex]
    return pIndex

if __name__ == '__main__':
    a = [12,21,314,53,12,54,89,43,2,67]
    print(quicksort(a, 0, 9))
    doctest.testmod()
