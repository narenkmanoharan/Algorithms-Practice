def unique(nums):
    cnt = {}
    for x in nums:
        if x in cnt:
            cnt[x] += 1
        else:
            cnt[x] = 1
    for i, x in enumerate(nums):
        if cnt[x] == 1:
            return i, x

if __name__ == '__main__':
    x, y = unique([1,3,4,2,1,3,2])
    print(x, y)
