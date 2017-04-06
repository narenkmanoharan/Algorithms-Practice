from collections import OrderedDict


def freq(nums):
    freq_dict = OrderedDict()
    for x in nums:
        if x in freq_dict:
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    return freq_dict


if __name__ == '__main__':
    x = [2, 3, 4, 2, 2, 3, 3, 5, 6, 6, 6, 4, 7]
    fre = freq(x)
    print(fre)
