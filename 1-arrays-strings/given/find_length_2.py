def find_length(s: str):
    left = current = answer = 0
    for right in range(len(s)):
        if s[right] == '0':
            current += 1

        while current > 1:
            if s[left] == '0':
                current -= 1
            left += 1

        answer = max(answer, right - left + 1)

    return answer
