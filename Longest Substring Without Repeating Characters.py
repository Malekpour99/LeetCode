def lengthOfLongestSubstring(s: str) -> int:
    sub1 = {}
    sub2 = {}
    i = 0
    while i < len(s):
        if s[i] not in sub1:
            sub1[s[i]] = i
            i += 1
        else:
            if len(sub1) > len(sub2):
                sub2 = sub1.copy()

            if i - sub1[s[i]] > 1:
                i = sub1[s[i]] + 1
                sub1.clear()
            else:
                sub1.clear()
                sub1[s[i]] = i
                i += 1
                
    return max(len(sub1), len(sub2))
