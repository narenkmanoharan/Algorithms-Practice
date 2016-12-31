import doctest
def merge_sort(lst):
    '''
    Returns a sorted list using merge function

    >>> merge_sort([122,12,542,123,52,12])
    [12, 12, 52, 122, 123, 542]

    '''
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    '''
    Takes two sorted lists and returns a single sorted list by comparing the elements one at a time.

    >>> left = [1, 5, 6]
    >>> right = [2, 3, 4]
    >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]

    '''
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    print(merge_sort([12,12352,2341,1,57,12,9,34,5,13,354,678,342]))
