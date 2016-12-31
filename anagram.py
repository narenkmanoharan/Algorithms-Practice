import doctest
def anagram(string1, string2):
    '''
    Returns true if the strings are anagrams else false
    
    >>> anagram('clear', 'rleac')
    True

    >>> anagram('potato','toasda')
    False
    '''

    if len(string1) != len(string2):
        return False
    dict_1 = {}
    for x in string1:
        if x in dict_1:
            dict_1[x] += 1
        else:
            dict_1[x] = 1           
    
    dict_2 = {}
    for x in string2:
        if x in dict_2:
            dict_2[x] += 1
        else:
            dict_2[x] = 1           

    if dict_1.keys() != dict_2.keys():
          return False
    else:
        keys = dict_1.keys()
        for x in keys:
            if dict_1[x] == dict_2[x]:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    an = anagram('cat', 'ccat')
    print(an)
    doctest.testmod()
