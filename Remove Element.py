def removeElement(nums: list[int], val: int) -> int:
    i, k = len(nums) - 1, len(nums)
    while i >= 0:
        if nums[i] == val:
            nums.pop(i)
            nums.append("_")
            k -= 1
        i -= 1
    return k
