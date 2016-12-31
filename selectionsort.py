import doctest
def selection_sort(lst):
    '''
    Returns a sorted list using selection sort

    >>> selection_sort([2,40,23,12,45,1]
    [1, 2, 12, 23, 40, 45]

    '''

    for x in range(len(lst)-1, 0, -1):
        max  = 0
        for i in range(1, x+1):
            if lst[i] > lst[max]:
                max = i
        lst[x], lst[max] = lst[max], lst[x]
    return lst

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    print(selection_sort([12,31,12,24,536,321,12,1]))
