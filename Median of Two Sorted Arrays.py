# first solution -> O(n+m log(n+m))
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    total_nums = sorted(nums1 + nums2)
    total_length = len(total_nums)
    if total_length % 2 == 1:
        med = (total_length // 2, total_length // 2)
    else:
        med = (total_length // 2 - 1, total_length // 2)
    
    return (total_nums[med[0]] + total_nums[med[1]]) / 2
