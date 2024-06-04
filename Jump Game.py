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


# A simple optimized solution for Leet Code ->
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True
