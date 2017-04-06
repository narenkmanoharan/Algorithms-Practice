def zigzag(string, nRows):
    if nRows == 1:
        print(string)
    elif nRows == 2:
        first_row = ''
        second_row = ''
        for x in range(0, len(string)):
            if x % 2 == 0:
                first_row += string[x]
            else:
                second_row += string[x]
        print(first_row)
        print(second_row)
    else:
        spaces = nRows - 1
        count = 0
        start = 0
        level = 2 * nRows - 2
        while count < nRows and level > 0:
            count += 1
            s=''
            for x in range(start, len(string), level):
                s += string[x] + ' '*spaces
            print(s)
            spaces -=1
            start += 1
            level -=2


if __name__ == '__main__':
    zigzag('sdasfadsfsdf', 5)
