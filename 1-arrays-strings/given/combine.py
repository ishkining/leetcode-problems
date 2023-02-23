def combine(first_nums: list[int], second_nums: list[int]) -> list[int]:
    i = 0
    j = 0
    result_nums = []

    while i < len(first_nums) and j < len(second_nums):
        if first_nums[i] >= second_nums[j]:
            result_nums.append(second_nums[j])
            j += 1
        else:
            result_nums.append(first_nums[i])
            i += 1

    while i < len(first_nums):
        result_nums.append(first_nums[i])
        i += 1

    while j < len(second_nums):
        result_nums.append(second_nums[j])
        j += 1

    return result_nums
