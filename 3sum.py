def three_sum(nums, target):
    end = len(nums) - 1
    for x in range(end):
        start = x + 1
        while start < end:
            val = nums[start] + nums[end] + nums[x]
            if target < val:
                end -= 1
            elif target > val:
                start += 1
            elif target == val:
                return [x, start, end]
            else:
                continue
    return -1


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums.sort()
    print(nums)
    x = three_sum(nums, 0)
    print(x)
