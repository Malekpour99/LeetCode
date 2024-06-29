def singleNumber(nums: list[int]) -> int:
    num_map = {}
    for i in range(len(nums)):
        if nums[i] not in num_map:
            num_map[nums[i]] = 1
        else:
            num_map[nums[i]] += 1

    return min(num_map, key=num_map.get)
