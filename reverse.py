import doctest

def rev(num):
    '''
    Prints the exact reverse of an integer

    >>> rev(123)
    321

    >>> rev(-123)
    -321

    >>> rev(12340)
    4321

    >>> rev(000)
    0

    '''
    if num is 0:
        return 0
    elif num > 0:
        n = str(num)
        n = reverse(n)
        n = int(n)
        return n
    else:
        n = str(num)
        n = reverse(n)
        n = int(n[:-1])
        return -n

def reverse(string):
    '''

    >>> reverse('naren')
    'neran'

    '''
    new = ''
    for x in range(len(string)-1, -1, -1):
        new += string[x]
    return new

if __name__ == '__main__':
    doctest.testmod()
    print(rev(102))
