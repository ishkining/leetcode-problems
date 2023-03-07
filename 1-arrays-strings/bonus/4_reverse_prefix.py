def reverse_prefix(word: str, ch: str) -> str:
    list_letters = list(word)
    left = 0
    right = len(list_letters) - 1
    list_letters = list(word)
    ch_index = -1
    for i in range(len(list_letters)):
        if list_letters[i] == ch:
            ch_index = i
            break

    for i in range(0, (ch_index // 2) + 1):
        list_letters[i], list_letters[ch_index - i] = list_letters[ch_index - i], list_letters[i]

    return ''.join(list_letters)
