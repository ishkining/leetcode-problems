def find_numbers(nums: list[int]) -> list[int]:
    answer = []
    nums = set(nums)

    for number in nums:
        if (number + 1 not in nums) and (number - 1 not in nums):
            answer.append(number)

    return number
