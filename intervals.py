def intervals(inter):
    if inter == []:
        return []
    inter.sort(key = lambda x: x[0])
    result = [inter[0]]
    for i in range(1, len(inter)):
        i1, i2 = [result[-1], inter[i]]
        if i2[0] > i1[-1]:
            result.append(i2)
        elif i2[-1] >= i1[-1]:
            i1[-1] = i2[-1]
    return result

if __name__ == '__main__':
    x = intervals([[1,3],[2,6],[8,10],[15,18]])
    print(x)
