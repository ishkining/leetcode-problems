def find_length(nums: list[int], k: int) -> int:
    left = current = answer = 0
    for right in range(len(nums)):
        current += nums[right]

        while current > k:
            current -= nums[left]
            left += 1

        answer = max(answer, right - left + 1)

    return answer
