def canJump(nums: list[int]) -> bool:
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False
    max_reach = 0
    total_length = len(nums) - 1
    for i in range(total_length):
        if total_length - i - nums[i] <= 0:
            return True
        if i + nums[i] > max_reach:
            max_reach = i + nums[i]
        if nums[i] == 0:
            if max_reach <= i:
                return False
    return False
