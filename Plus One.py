def plusOne(digits: list[int]) -> list[int]:
    i = len(digits) - 1
    carry = 0
    carry, digits[i] = divmod(digits[i] + 1, 10)
    while carry:
        i = i - 1 if i - 1 >= 0 else None
        try:
            carry, digits[i] = divmod(digits[i] + carry, 10)
        except TypeError:
            digits.insert(-1, carry)
            carry = 0

    return digits


print(plusOne([9]))
