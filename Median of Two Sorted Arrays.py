# first solution -> O(n+m log(n+m))
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    total_nums = sorted(nums1 + nums2)
    total_length = len(total_nums)
    if total_length % 2 == 1:
        med = (total_length // 2, total_length // 2)
    else:
        med = (total_length // 2 - 1, total_length // 2)

    return (total_nums[med[0]] + total_nums[med[1]]) / 2


# two pointer solution -> O(log(n+m))
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    n, m = len(nums1), len(nums2)
    total_length = len(nums1) + len(nums2)
    p1, p2 = 0, 0
    med1 = 0
    med2 = 0
    for _ in range(total_length // 2 + 1):
        med2 = med1
        if p1 < n and p2 < m:
            if nums1[p1] > nums2[p2]:
                med1 = nums2[p2]
                p2 += 1
            else:
                med1 = nums1[p1]
                p1 += 1
        elif p1 < n:
            med1 = nums1[p1]
            p1 += 1
        elif p2 < m:
            med1 = nums2[p2]
            p2 += 1

    if total_length % 2 == 0:
        return (med1 + med2) / 2
    else:
        return float(med1)
