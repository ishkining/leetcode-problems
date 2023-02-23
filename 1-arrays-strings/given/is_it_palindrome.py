def is_it_palindrome(line: str):
    left = 0
    right = len(line) - 1

    while left < right:
        if line[left] == line[right]:
            left += 1
            right -= 1
        else:
            return False

    return True
