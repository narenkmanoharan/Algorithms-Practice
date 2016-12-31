import doctest
def bubblesort(lst):
    """
    Performs bubble sort on the given list

    >>> bubblesort([1,23,2,15,35,6])
    [1, 2, 6, 15, 23, 35]
    """
    for x in range(len(lst) - 1, 0, -1):
        for y in range(x):
            if lst[y] > lst[y+1]:
                lst[y], lst[y+1] = lst[y+1], lst[y]

    return lst

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    lst = [12,234,534,12,4123,4254,2344,21,13]
    print(bubblesort(lst))

