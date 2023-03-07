def equal_substring(s: str, t: str, max_cost: int) -> int:
    letters_input = list(s)
    letters_output = list(t)
    answer = current = left = 0
    for right in range(len(s)):
        current += abs(ord(letters_input[right]) - ord(letters_output[right]))

        while current > max_cost:
            current -= abs(ord(letters_input[left]) - ord(letters_output[left]))
            left += 1

        answer = max(answer, right - left + 1)

    return answer
