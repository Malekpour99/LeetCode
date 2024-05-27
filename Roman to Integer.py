def romanToInt(s: str) -> int:
    roman_value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_value_map[s[i]] < roman_value_map[s[i + 1]]:
            ans -= roman_value_map[s[i]]
        else:
            ans += roman_value_map[s[i]]
    return ans


print(romanToInt("III"))  # 3
print(romanToInt("LVIII"))  # 58
print(romanToInt("MCMXCIV"))  # 1994
