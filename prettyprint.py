import doctest
def pretty(func):
    """
    A function that outputs the given values in a pretty manner
    """

    def inner_func(string_names):
        a,b,c,d,e,f = func(string_names)
        result = "{} {} and {} {} are going to {} {} class today!".format(a,b,c,d,e,f)
        return result
    return inner_func

@pretty
def names(string_name):
    """
    This function splits the given string with spaces to produce the names.
    """
    dix,y,a,b,p,q = string_names.split(' ')
    return x,y,a,b,p,q

if __name__ == "__main__":
    value = names(input("Please enter the name string with spaces: "))
    print(value)
    doctest.testmod(verbose=True)
