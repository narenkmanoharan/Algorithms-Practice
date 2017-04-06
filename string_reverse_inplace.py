def rev(s):
    li = []
    li.extend(s)
    x = len(li)
    for y in range(int(x/2)):
        li[y], li[x-1-y] = li[x-1-y], li[y]
    s = ''.join(li)
    print(s)
if __name__ == '__main__':
    x = 'narendra kumar manoharan'
    rev(x)
