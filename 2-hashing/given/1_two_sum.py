def two_sum(nums: list[int], target: int) -> list[int]:
    diff_target = {}
    for i, number in enumerate(nums):
        complement = target - number
        if complement in diff_target:
            return [i, diff_target[complement]]

        diff_target[complement] = i

    return [-1, -1]

