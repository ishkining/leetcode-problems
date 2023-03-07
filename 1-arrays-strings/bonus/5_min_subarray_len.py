def min_subarray_len(target: int, nums: list[int]) -> int:
    left = current = 0
    answer = len(nums) + 1
    for right in range(len(nums)):
        current += nums[right]

        while current >= target:
            answer = min(answer, right - left + 1)
            current -= nums[left]
            left += 1

    return answer if answer != len(nums) + 1 else 0
