import doctest
def seq_search(nums, find):
    """
    Performs a sequential search on the numbers and return the index if foundi
    and -1 is not.

    >>> seq_search([1,2,3,4],3)
    2

    >>> seq_search([10,2130,1203,1320],20)
    -1
    """
    index = [x for x in range(0,len(nums)) if nums[x] == find]
    if index == []:
        return -1
    return index[0]

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    nums = map(float, input("Please enter the numbers in the list: ").split( ))
    list = [x for x in nums]
    find = float(input("Enter the number to be searched: "))
    res = seq_search(list, find)
    print(res)
