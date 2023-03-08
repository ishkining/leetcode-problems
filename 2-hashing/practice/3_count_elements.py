def count_elements(arr: list[int]) -> int:
    seen = set(arr)
    answer = 0
    for number in arr:
        if number + 1 in seen:
            answer += 1

    return answer
