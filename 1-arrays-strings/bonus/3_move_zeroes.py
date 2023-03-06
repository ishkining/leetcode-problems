def moveZeroes(nums: list[int]) -> None:
    i = 0
    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1

    for i in range(i, len(nums)):
        nums[i] = 0
