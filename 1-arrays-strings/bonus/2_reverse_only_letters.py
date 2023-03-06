def reverse_only_letters(s: str) -> str:
    result = list(s)
    letters = []
    for i in range(len(result)):
        if 96 < ord(result[i]) < 123 or 64 < ord(result[i]) < 91:
            letters.append(result[i])
            result[i] = 'A'

    counter = 1
    for i in range(len(result)):
        if result[i] == 'A':
            result[i] = letters[-1 * counter]
            counter += 1
    return ''.join(result)