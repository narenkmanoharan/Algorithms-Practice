def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    if sum(nums) < s:
        return 0
    end = len(nums)
    res = end
    l = r = tot = 0
    while r <= end:
        if tot < s:
            if r < end:
                tot += nums[r]
            r += 1
        else:
            res = min(res, r - l)
            tot -= nums[l]
            l += 1
    return res

if __name__ == '__main__':
    x = minSubArrayLen(11, [1, 2, 3, 4, 15])
    print(x)
