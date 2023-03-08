def missing_number(nums: list[int]) -> int:
    set_nums = set(nums)
    ending = len(nums) + 1
    for number in range(ending):
        if number not in set_nums:
            return number
