def longestCommonPrefix(strs: list[str]) -> str:
    lcp = ""
    temp_lcp = ""
    i = 0
    while True:
        try:
            temp_lcp = strs[0][i]
            for word in strs:
                if word[i] != temp_lcp:
                    return lcp
        except IndexError:
            return lcp
        lcp += temp_lcp
        i += 1


# Optimized solution from Leet Code
class Solution:
    def longestCommonPrefix(self, v: list[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans
