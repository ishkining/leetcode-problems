def pivot_index(self, nums: list[int]) -> int:
    prefix_sum = [nums[-1]]
    for i in range(len(nums) - 2, -1, -1):
        prefix_sum.append(nums[i] + prefix_sum[-1])
    print(prefix_sum)
    pivot_sum = 0
    for i in range(len(nums)):

        if pivot_sum == prefix_sum[(-1 * i) - 1] - nums[i]:
            return i
        pivot_sum += nums[i]

    return -1
