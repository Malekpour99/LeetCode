def majorityElement(nums: list[int]) -> int:
    nums_hash = {}
    for i in range(len(nums)):
        if nums[i] not in nums_hash:
            nums_hash[nums[i]] = 1
        else:
            nums_hash[nums[i]] += 1
    # returning the key with the highest value
    return max(nums_hash, key=nums_hash.get)
