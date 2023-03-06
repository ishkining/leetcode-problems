def reverseWords(s: str) -> str:
    list_words = s.split()
    answer = ''
    for word in list_words:
        answer += word[::-1] + ' '
    return answer[:-1]
