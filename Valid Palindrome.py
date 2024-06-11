def isPalindrome(s: str) -> bool:
    phrase = ""
    for c in s:
        if c.isalnum():
            phrase += c.lower()

    for i in range(len(phrase) // 2):
        if phrase[i] != phrase[-1 - i]:
            return False

    return True
