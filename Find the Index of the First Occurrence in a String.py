def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


def strStr(haystack: str, needle: str) -> int:
    n = len(haystack)
    m = len(needle)

    # Edge case: if the substring is empty, return 0
    if m == 0:
        return 0

    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return i

    # If the substring is not found, return -1
    return -1
