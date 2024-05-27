def removeDuplicates(nums: list[int]) -> int:
    nums_hash = {}
    i, k = len(nums) - 1, len(nums)
    while i >= 0:
        if nums[i] in nums_hash and nums_hash[nums[i]] == 2:
            nums.pop(i)
            nums.append("_")
            k -= 1
        elif nums[i] in nums_hash:
            nums_hash[nums[i]] += 1
        else:
            nums_hash[nums[i]] = 1
        i -= 1
    return k
