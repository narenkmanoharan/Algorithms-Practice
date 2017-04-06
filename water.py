def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)
    l, r, water, minHeight = 0, n - 1, 0, 0
    while l < r:
        while l < r and height[l] <= minHeight:
            water += minHeight - height[l]
            l += 1
        while l < r and height[r] <= minHeight:
            water += minHeight - height[r]
            r -= 1
        minHeight = min(height[l], height[r])
    return water


if __name__ == '__main__':
    res = trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(res)
