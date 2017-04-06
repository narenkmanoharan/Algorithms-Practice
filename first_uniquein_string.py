def unique(a):
    d = {}
    for i in range(len(a)):
        x = a[i]
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for i, y in enumerate(s):
        if d[y] == 1:
            return i


if __name__ == '__main__':
    s = 'naren'
    print(unique(s))
