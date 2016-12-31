import doctest
def insertion_sort(lst):
    '''
    Returns a sorted list using insertion sort

    >>> insertion_sort([12,23,42,412,14,31,1,344,123])
    [1, 12, 14, 23, 31, 42, 123, 344, 412]

    '''
    for i in range(1, len(lst)):
        current = lst[i]
        index = i
        while lst[index-1] > current and index > 0:
            lst[index] = lst[index-1]
            index = index - 1
        lst[index] = current
    return lst

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    print(insertion_sort([121,54,23,76234,678,1236,345,97132,576]))
