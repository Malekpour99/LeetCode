def removeDuplicates(nums: list[int]) -> int:
    nums_hash = {}
    i, k = len(nums) - 1, len(nums)
    while i >= 0:
        if nums[i] in nums_hash:
            nums.pop(i)
            nums.append("_")
            k -= 1
        else:
            nums_hash[nums[i]] = i
        i -= 1
    return k
