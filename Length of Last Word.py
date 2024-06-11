def lengthOfLastWord(s: str) -> int:
    words = s.split()
    return len(words[-1])
