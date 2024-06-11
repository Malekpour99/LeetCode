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
