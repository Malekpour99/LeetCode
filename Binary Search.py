def search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums)
    while low < high:
        mid = (high + low) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid
    
    # If target was not found
    return -1
