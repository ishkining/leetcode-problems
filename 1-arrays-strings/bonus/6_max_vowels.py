def max_vowels(s: str, k: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    current = 0
    list_letters = list(s)
    for i in range(k):
        if list_letters[i] in vowels:
            current += 1

    answer = current
    for i in range(k, len(s)):
        if list_letters[i - k] in vowels:
            current -= 1
        if list_letters[i] in vowels:
            current += 1
        answer = max(answer, current)

    return answer
