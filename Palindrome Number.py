def isPalindrome(x: int) -> bool:
    string_num = str(x)
    for i in range(len(string_num) // 2):
        if string_num[i] != string_num[len(string_num) - (i + 1)]:
            return False
    return True


