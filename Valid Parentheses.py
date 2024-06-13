def isValid(s: str) -> bool:
    pair_hash = {"{": "}", "[": "]", "(": ")"}
    opened = []
    for char in s:
        if char in pair_hash:
            opened.append(char)
        else:
            try:
                if char != pair_hash[opened.pop()]:
                    return False
            except IndexError:
                return False
    if len(opened):
        return False
    return True
