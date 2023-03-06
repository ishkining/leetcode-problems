def ways_to_split_array(nums: list[int]) -> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    answer = 0
    for i in range(len(nums) - 1):
        left_section = prefix[i]
        right_section = prefix[-1] - left_section
        if left_section >= right_section:
            answer += 1

    return answer
