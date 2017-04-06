def dup(a, b):
    if abs(len(a) - len(b)) > 1:
        return -1
    res = 0
    for x in a:
        res = res^x
    for y in b:
        res = res^y
    return res

if __name__ == '__main__':
    x = [2, 3, 7, 1, 4, 5]
    y = [2, 3, 7, 4, 5]
    print(dup(x,y))
