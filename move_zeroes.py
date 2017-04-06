def zero(li):
    i = 0
    j = 1
    while j < len(li):
        if li[i] == 0 and li[j] != 0:
            li[i], li[j] = li[j], li[i]
            i += 1
            j += 1
        elif li[j] == 0 and li[i] == 0:
            j += 1
        else:
            i += 1
            j += 1
    return li


if __name__ == '__main__':
    z = [2, 4, 0, 2, 3, 0, 0, 2, 0, 1, 0]
    x = [0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 2, 2, 3, 4, 1]
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    b = [1, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    print(zero(b))
