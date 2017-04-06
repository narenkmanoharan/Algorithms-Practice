def max_sorted_array(nums, low, high):
    if len(nums) < 1:
        return None
    if high < low:
        return nums[0]
    if high == low:
        return nums[high]
    mid = low + (high - low) // 2
    if mid < high and nums[mid+1] < nums[mid]:
        return mid
    if mid > low and nums[mid-1] > nums[mid]:
        return mid - 1
    if nums[mid] < nums[high]:
        return max_sorted_array(nums, low, mid-1)
    return max_sorted_array(nums, mid+1, high)

if __name__ == '__main__':
    print(max_sorted_array([3,4,5,1,2], 0 , 4))
    print(max_sorted_array([], 0, 0))
    print(max_sorted_array([1,2,3,4,5], 0, 4))
    print(max_sorted_array([3,4,5], 0 , 2))
    print(max_sorted_array([1,1,1,1,1,1],0,5))
