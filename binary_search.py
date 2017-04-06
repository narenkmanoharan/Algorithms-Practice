def bin(nums, low, high, key):
    if high < low:
        return -1
    mid = low + (high - low) // 2
    if nums[mid] == key:
        return mid
    if nums[mid] < key:
        return bin(nums, mid+1, high, key)
    return bin(nums, low, mid-1, key)

if __name__ == '__main__':
    print(bin([1,2,3,4,5], 0, 4, 4))
