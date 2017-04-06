import sys,doctest
def multiply(x,y):
    '''
    Returns the multiplication fo the two numbers.
    >>> multiply(5,2)
    10
    '''
    return int(x)*int(y)

if __name__ == '__main__':
    x,y=sys.argv[1], sys.argv[2]
    print(multiply(x,y))
    doctest.testmod(verbose=True)
    
