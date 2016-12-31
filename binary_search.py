import doctest
def bin_src(lst, num, start, end):
    '''
    Performs a binary seach on the given list for the given num
    >>> bin_src([1,2,3,45,50], 3, 0, 4)
    Found at index 2
    '''
    mid_index = start + (end - start) // 2
    if start > end:
        return 'Not Found'
    if lst[mid_index] is num:
        print("Found at index " + str(mid_index))
        return
    if lst[mid_index] > num:
        bin_src(lst, num, 0, mid_index-1)
    else:
        bin_src(lst, num, mid_index + 1, len(lst)-1)

if __name__ == '__main__':
    doctest.testmod()
    lst = list(map(int, input("Please enter the list with spaces: ").split()))
    print("The list you have entered is: {}".format(lst))
    num = int(input("Please enter the num to be found: "))
    bin_src(lst, num, 0, len(lst)-1)
