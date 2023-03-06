def find_best_subarray(nums: list[int], k: int) -> int:
    current = 0
    for i in range(k):
        current += nums[i]

    answer = current
    for i in range(k, len(nums)):
        current += nums[i] - nums[i-k]
        answer = max(current, answer)

    return answer
