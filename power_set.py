def power_set(val):
    pow_set = [[]]
    for x in val:
        p = len(pow_set)
        for i in range(p):
            value = pow_set[i]
            a = value + [x]
            pow_set.append(a)
    return pow_set

if __name__ == '__main__':
    x = ['a', 'b', 'c']
    res = power_set(x)
    print(res)