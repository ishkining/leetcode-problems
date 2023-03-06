def minStartValue(nums: list[int]) -> int:
    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[-1])

    answer = 0
    for value in prefix_sum:
        answer = min(answer, value)

    return (-1 * answer) + 1
