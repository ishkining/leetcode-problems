def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0

    left = answer = 0
    current = 1

    for right in range(len(nums)):
        current *= nums[right]

        while current >= k:
            current //= nums[left]
            left += 1

        answer += right - left + 1

    return answer
