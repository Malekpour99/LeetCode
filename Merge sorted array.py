def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1_copy = nums1.copy()
    i, j, k = 0, 0, 0
    while i < m and j < n:
        if nums2[j] < nums1_copy[i]:
            nums1[k] = nums2[j]
            j += 1
        else:
            nums1[k] = nums1_copy[i]
            i += 1
        k += 1
    while i < m:
        nums1[k] = nums1_copy[i]
        i += 1
        k += 1
    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1


# A better solution is to use these pointers from the end to the start
# It was one of the good solutions
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
