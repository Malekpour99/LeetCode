def twoSum(nums: list[int], target: int) -> list[int]:
    for num in nums:
        if target - num in nums[nums.index(num) + 1 :]:
            return [nums.index(num), nums.index((target - num), nums.index(num) + 1)]
    return []


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
print(twoSum([-1, -2, -3, -4, -5], -8))
