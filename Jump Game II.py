def jump(nums: list[int]) -> int:
    jump_count = 0
    if len(nums) == 1:
        return jump_count
    jump_power = 0
    reach = 0
    target = len(nums) - 1
    for i in range(target):
        if nums[i] + i > jump_power:
                jump_power = nums[i] + i
        if target - jump_power <= 0:
            jump_count += 1
            return jump_count
        if i == reach:
            jump_count += 1
            reach = jump_power

# [3,4,1,1,1,1,1]
# [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]

def jump(nums: list[int]) -> int:
    jump_count = 0
    jump_power = 0
    reach = 0
    target = len(nums) - 1
    for i in range(target):
        if nums[i] + i > jump_power:
                jump_power = nums[i] + i
        if target - jump_power <= 0:
            jump_count += 1
            break
        if i == reach:
            jump_count += 1
            reach = jump_power
    
    return jump_count
