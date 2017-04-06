import doctest

def two_sum(nums, target):
    '''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target

    >>> two_sum([2, 7, 11, 15], target=9)
    (0, 1)

    >>> two_sum([1,2,4,8,32,64], target=12)
    (2, 3)

    >>> two_sum([1,2,3,6,12], target=10)
    'Not Found'

    '''
    last = len(nums) - 1
    start = 0
    for i in range(last):
        current_val = nums[last] + nums[start]
        if current_val == target:
            return start, last
        elif current_val < target:
            start += 1
        elif current_val > target:
            last -=1
    return 'Not Found'

if __name__ == '__main__':
    doctest.testmod()
    lst = [1,6,10,21,36,57]
    print(two_sum(lst, 16))
